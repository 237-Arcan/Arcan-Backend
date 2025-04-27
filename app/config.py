class Config(object):
    SECRET_KEY = "change-me"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
