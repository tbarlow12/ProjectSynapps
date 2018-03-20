class Config(object):
    DEVELOPMENT = True
    DEBUG = True
    ACCOUNT_NAME = 'accountname'
    ACCOUNT_KEY = 'accountkey'

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    ACCOUNT_NAME = 'accountname'
    ACCOUNT_KEY = 'accountkey'