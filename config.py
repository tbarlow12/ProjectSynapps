class Config(object):
    DEVELOPMENT = True
    DEBUG = True
    ACCOUNT_NAME = 'defaultname'
    ACCOUNT_KEY = 'defaultkey'

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    ACCOUNT_NAME = 'tabarlowtest'
    ACCOUNT_KEY = '7nas/GOi6XP2gaUIoHj0JPbAEYHzgCDSD5DxHXPfb0k1GclsZmbzYuRAyctQ2NooQuqLnmJzbGnqxxv7xtcMgw=='