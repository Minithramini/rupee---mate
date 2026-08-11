import os
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from config import Config
from models import db, auto_migrate_schema

# Blueprint imports
from routes.auth import auth_bp
from routes.expenses import expenses_bp
from routes.incomes import incomes_bp
from routes.budgets import budgets_bp
from routes.category_budgets import category_budgets_bp
from routes.categories import categories_bp
from routes.analytics import analytics_bp
from routes.savings import savings_bp
from routes.recurring import recurring_bp
from routes.export import export_bp
from routes.ai import ai_bp
from routes.groups import groups_bp
from routes.sms_parser import sms_parser_bp

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(config_class)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload
    
    CORS(app, supports_credentials=True)
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(expenses_bp)
    app.register_blueprint(incomes_bp)
    app.register_blueprint(budgets_bp)
    app.register_blueprint(category_budgets_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(savings_bp)
    app.register_blueprint(recurring_bp)
    app.register_blueprint(export_bp)
    app.register_blueprint(ai_bp)
    app.register_blueprint(groups_bp)
    app.register_blueprint(sms_parser_bp)
    
    # Global Error Handlers
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({'success': False, 'error': 'Bad Request: ' + str(e.description if hasattr(e, 'description') else 'Invalid parameters')}), 400

    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify({'success': False, 'error': 'Unauthorized: Please log in to proceed'}), 401

    @app.errorhandler(403)
    def forbidden(e):
        return jsonify({'success': False, 'error': 'Forbidden: You do not have permission'}), 403

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'success': False, 'error': 'Resource not found'}), 404

    @app.errorhandler(409)
    def conflict(e):
        return jsonify({'success': False, 'error': str(e.description if hasattr(e, 'description') else 'Conflict detected')}), 409

    @app.errorhandler(422)
    def unprocessable(e):
        return jsonify({'success': False, 'error': 'Unprocessable entity: Validation failed'}), 422

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({'success': False, 'error': 'Internal server error. Please try again later.'}), 500
        
    # Frontend & PWA Routes
    @app.route('/')
    def index():
        return send_from_directory('templates', 'index.html')
        
    @app.route('/manifest.json')
    def manifest():
        return send_from_directory('static', 'manifest.json', mimetype='application/json')

    @app.route('/sw.js')
    def service_worker():
        response = send_from_directory('static', 'sw.js', mimetype='application/javascript')
        response.headers['Service-Worker-Allowed'] = '/'
        return response
        
    @app.route('/<path:path>')
    def serve_static(path):
        if os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        return send_from_directory('templates', 'index.html')
        
    with app.app_context():
        # Ensure uploads folder exists
        os.makedirs(os.path.join(app.static_folder, 'uploads', 'receipts'), exist_ok=True)
        auto_migrate_schema(app)
        
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)