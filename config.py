import os
from decouple import config

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'src/static/uploads')
DATABASE_URI = f'mysql+pymysql://{config("DB_USER")}:{config("DB_PASSWORD")}@{config("DB_HOST")}:{config("DB_PORT")}/{config("DB_NAME")}'


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = config("SECRET_KEY", default="top-secret")
    SECURITY_PASSWORD_SALT = config("SECURITY_PASSWORD_SALT", default="guess-me")
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    UPLOAD_FOLDER = UPLOAD_FOLDER

    SESSION_TYPE = config("SESSION_TYPE", default="sqlalchemy")
    SESSION_USE_SIGNER = config("SESSION_USE_SIGNER", default=True)

    # Redis caching configuration
    CACHE_TYPE = "redis"  # Specify the cache type as redis
    CACHE_REDIS_HOST = config("CACHE_REDIS_HOST", default="localhost")  # Redis server host
    CACHE_REDIS_PORT = config("CACHE_REDIS_PORT", default=6379)  # Redis server port
    CACHE_REDIS_DB = config("CACHE_REDIS_DB", default=0)  # Redis database number
    CACHE_DEFAULT_TIMEOUT = config("CACHE_DEFAULT_TIMEOUT", default=604800)  # Default cache timeout (in seconds)


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False
