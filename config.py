import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-student-finance-key-super-secret-2026')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///student_finance.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session and Cookie Security
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = os.environ.get('FLASK_ENV') == 'production'
    PERMANENT_SESSION_LIFETIME = 86400 * 7  # 7 days
    
    # Google OAuth Configuration
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', '')
    
    # Optional AI Service Key
    AI_API_KEY = os.environ.get('AI_API_KEY', None)
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')