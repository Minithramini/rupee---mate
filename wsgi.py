import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    try:
        # Use Waitress if available (ideal for Windows & cross-platform)
        from waitress import serve
        print(f"Serving RupeeMate on port {port} with Waitress production server...")
        serve(app, host='0.0.0.0', port=port)
    except ImportError:
        # Fall back to built-in server
        app.run(host='0.0.0.0', port=port)
