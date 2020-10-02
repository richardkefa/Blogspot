import os
class Config:
  '''
  general configuration 
  '''
  SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:Access@localhost/blog'
  SECRET_KEY = os.environ.get('SECRET_KEY') 
  QUOTES_API_URL=os.environ.get('QUOTES_API_URL')
  
  #  email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  
class ProdConfig(Config):
  '''
  production configuration
  '''
  SQLALCHEMY_DATABASE_URI =os.environ.get("DATABASE_URL")
class DevConfig(Config):
  '''
  development configurations
  '''
  SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:Access@localhost/blog'
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production':ProdConfig
    
}

  