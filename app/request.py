import requests
def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
      return response.json()
    else:
      return ['Greatness requires internal toughness','David']
      
  