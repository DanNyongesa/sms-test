# -*-coding:utf-8-*-
'''Configuration file'''


class Config(object):
    '''Base configuration'''
    DEBUG = True
    TESTING = False

    @classmethod
    def init_app(cls, app):
        '''custom classmethod'''
        pass


class Development(Config):
    '''Development mode'''
    pass


class Production(Config):
    '''Production mode'''
    DEBUG = False


class Testing(Config):
    '''Testing mode'''
    TESTING = True


CONFIG = {
    'development': Development,
    'testing': Testing,
    'production': Production,

    'default': Development
}
