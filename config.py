#coding: utf-8
class Config():
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "mysql://root:caomu888@localhost:3306/mysql"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True