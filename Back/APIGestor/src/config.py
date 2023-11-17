class DevelopmentConfig:
    ##DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@database:3306/tareas'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig
}
