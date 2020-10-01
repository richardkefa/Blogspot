import urllib.request, json
from .models import Quotes
from flask import render_template

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
    
    quote_results = process_results(get_quote_response)
    
  return quote_results

def process_results(quote_list):
  '''
  function to processes the quote result
  '''
  quote_result =[]
  for quote_item in quote_list
  author = quote_item.get('author')
  quote = quote_item.get('quote')
    
  quote_object = Quotes(id,author)
  quote_result.append(quote_object)
  
  return quote_result

  