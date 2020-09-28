import urllib.request, json
from .models import Quotes

base_url=None

def Configure_request(app):
  global base_url
  base_url = app.config['QUOTES_API_URL']
  
def get_quote():
  '''
  getting api response
  '''
  with urllib.request.urlopen(base_url) as url:
    get_quote_data = url.read()
    get_quote_response = json.loads(get_quote_data)
    
    quote_results = None
    
    quote_results_list = get_quote_response
    
  