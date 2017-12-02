# -*-coding:utf-8-*-
'''Configuration file'''


class Config(object):
    '''Base configuration'''
    debug = True

    @classmethod
    def init_app(cls, app):
        '''custom classmethod'''
        pass


class Development(Config):
    '''Development mode'''
    pass


class Production(Config):
    '''Production mode'''
    debug = False


class Testing(Config):
    '''Testing mode'''
    Testing = True


CONFIG = {
    'development': Development,
    'testing': Testing,
    'production': Production,

    'default': Development
}
