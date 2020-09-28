import os
class Config:
  '''
  general configuration 
  '''
  SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:Access@localhost/blog'
  SECRET_KEY = os.environ.get('SECRET_KEY') 
  QUOTES_API_URL=os.environ.get('QUOTES_API_URL')
  
class ProdConfig(Config):
  '''
  production configuration
  '''
  pass
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

  