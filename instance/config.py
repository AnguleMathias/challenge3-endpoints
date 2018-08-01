import os


class Config(object):
    DEBUG = False
    SECRET = os.getenv('SECRET')
    host = os.getenv('DB_HOST')
    db = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')


class DevelopmentConfig(Config):
    DEBUG = True
    APP_SETTINGS = 'development'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE = os.getenv('TEST_NAME')
    APP_SETTINGS = 'testing'


class StagingConfig(Config):
    DEBUG = True
    APP_SETTINGS = 'staging'


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    APP_SETTINGS = 'production'


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
