import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.imdb.com/chart/top/')