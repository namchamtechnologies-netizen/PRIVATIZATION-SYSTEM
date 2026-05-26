"""
Django settings for dict project.

Optimized for local development (SQLite) and production on Railway (PostgreSQL)
"""

import os
import sys
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env file for local development
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ==================== SECURITY ====================

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-fallback-key-for-development-only-change-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False in production

# Host configurations - UPDATED with correct Railway domain
ALLOWED_HOSTS = [
    'privatization-system-production.up.railway.app',  # ADDED - the correct domain (with 'z')
    'privatisation-production.up.railway.app',        # Keep existing (with 's')
    'authority-production.up.railway.app',  
    'pa-mfalme-production.up.railway.app',
    '127.0.0.1',
    'localhost',
    'www.privatisation.go.ke',
    'privatisation.go.ke',
]

CSRF_TRUSTED_ORIGINS = [
    'https://privatization-system-production.up.railway.app',  # ADDED
    'https://privatisation-production.up.railway.app',
    'https://127.0.0.1',
    'https://localhost',
    'https://privatisation.go.ke',
    'https://www.privatisation.go.ke',
]

# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Security settings for production
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# ==================== APPLICATION DEFINITION ====================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your apps
    'myapp',
    
    # Third-party apps (optional)
      # If you need advanced CORS control
]

MIDDLEWARE = [
     # Must be before CommonMiddleware
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dict.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dict.wsgi.application'

# ==================== DATABASE ====================
# DIRECT POSTGRESQL CONFIGURATION - Using public Railway URL

# Hardcoded database URL from Railway
RAILWAY_DB_URL = 'postgresql://postgres:KGbbVXopumYpHDMBeAPsNdUHqeLCJrZA@zephyr.proxy.rlwy.net:38090/railway'

# Use environment variable if available, otherwise use hardcoded URL
DATABASE_URL = os.environ.get('DATABASE_URL', RAILWAY_DB_URL)

# Configure database - FORCE PostgreSQL for both local and production
DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        conn_health_checks=True,
        ssl_require=False  # Set to True if Railway requires SSL
    )
}

# ==================== PASSWORD VALIDATION ====================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ==================== INTERNATIONALIZATION ====================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ==================== STATIC FILES ====================
# Whitenoise configuration for Railway

STATIC_URL = '/static/'

# Static files directories
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Static root for collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Whitenoise compression and caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Cache static files for 1 year (recommended for Railway)
WHITENOISE_MAX_AGE = 31536000  # 1 year in seconds

# ==================== MEDIA FILES ====================

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ==================== EMAIL CONFIGURATION ====================

# Email settings - use environment variables for sensitive data
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'mail.privatisation.go.ke')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'False') == 'True'
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', 'True') == 'True'
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '465'))
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'info@privatisation.go.ke')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)

# ==================== DEFAULT PRIMARY KEY ====================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==================== LOGGING ====================
# Better logging for debugging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}

# ==================== DATABASE CONNECTION TEST ====================
# This will test the database connection when running Django commands

def test_database_connection():
    """Test database connection and display status"""
    try:
        from django.db import connections
        from django.core.management.color import color_style
        
        style = color_style()
        
        # Try to connect to the database
        connection = connections['default']
        connection.ensure_connection()
        
        # Get connection information
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            version = cursor.fetchone()[0]
            
            cursor.execute("SELECT current_database();")
            db_name = cursor.fetchone()[0]
            
            cursor.execute("SELECT inet_server_addr();")
            server_addr = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public';")
            table_count = cursor.fetchone()[0]
        
        # Print success message
        print("\n" + "="*70)
        print(style.SUCCESS("✅ DATABASE CONNECTION SUCCESSFUL!"))
        print("="*70)
        print(f"📊 Database Name: {style.SUCCESS(db_name)}")
        print(f"🐘 PostgreSQL Version: {style.SUCCESS(version.split(',')[0])}")
        print(f"🌐 Server Address: {style.SUCCESS(server_addr)}")
        print(f"📈 Tables in database: {style.SUCCESS(table_count)}")
        print(f"🔧 Database Engine: {style.SUCCESS(DATABASES['default']['ENGINE'])}")
        print(f"📍 Database Host: {style.SUCCESS(DATABASES['default'].get('HOST', 'localhost'))}")
        print("="*70 + "\n")
        
        return True
        
    except Exception as e:
        from django.core.management.color import color_style
        style = color_style()
        
        print("\n" + "="*70)
        print(style.ERROR("❌ DATABASE CONNECTION FAILED!"))
        print("="*70)
        print(style.ERROR(f"Error: {e}"))
        print("="*70)
        print("\nTroubleshooting tips:")
        print("1. Check if DATABASE_URL is correct in settings.py")
        print("2. Verify PostgreSQL server is running")
        print("3. Check if your IP is allowed to connect")
        print("4. Ensure psycopg2-binary is installed: pip install psycopg2-binary")
        print("="*70 + "\n")
        
        # Don't crash the server if DEBUG is False (production)
        if not DEBUG:
            print("⚠️  Warning: Continuing anyway (DEBUG=False mode)")
            return False
        else:
            print("🛑 Stopping due to DEBUG=True mode")
            sys.exit(1)

# Run database test only for specific management commands
test_commands = ['runserver', 'shell', 'check', 'createsuperuser', 'makemigrations', 'migrate']

if 'manage.py' in sys.argv and any(cmd in sys.argv for cmd in test_commands):
    # Initialize Django to test connection
    try:
        import django
        django.setup()
        test_database_connection()
    except Exception as e:
        print(f"Error during database test setup: {e}")