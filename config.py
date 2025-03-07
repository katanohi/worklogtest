# ここで各環境用の設定を作りたい


class Config(object):
    DEBUG = True
    SECRET_KEY = "secret-key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///memodb.sqlite"
