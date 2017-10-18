#coding: utf-8
class Config():
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
