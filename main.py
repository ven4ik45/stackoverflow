from datetime import timedelta, datetime
from pprint import pprint
import requests
import json

def two_days_ago():
      days_ago = int((datetime.today() - timedelta(days=2)).timestamp())
      return days_ago


url = f'https://api.stackexchange.com/2.3/questions?' \
      f'fromdate={two_days_ago()}&' \
      f'order=desc&' \
      f'sort=creation&' \
      f'tagged=Python&' \
      f'site=stackoverflow&' \
      f'filter=!nOedRLjYKj'
response = requests.get(url=url).content
data = json.loads(response)

pprint(data)
