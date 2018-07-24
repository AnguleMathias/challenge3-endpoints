class Config:
    """Parent configuration class"""

    def __init__(self):
        pass

    DEBUG = False


class Development(Config):
    """Configuration for development environment"""
    DEBUG = True


class Testing(Config):
    """Configuration for testing environment"""
    DEBUG = True


app_config = {
    'development': Development,
    'testing': Testing,
}
