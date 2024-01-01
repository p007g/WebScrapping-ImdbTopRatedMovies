import requests
from bs4 import BeautifulSoup
import random


try:

    user_agents_list = [
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
]
    response = requests.get('https://www.imdb.com/chart/top/', headers={'User-Agent': random.choice(user_agents_list)})
    response.raise_for_status()

    data = BeautifulSoup(response.text, 'html.parser')

    movies = data.find('ul', class_="ipc-metadata-list").find_all('li', class_="ipc-metadata-list-summary-item")

    for movie in movies:

        rank = movie.find('h3', class_="ipc-title__text").text.split('. ')[0]
        name = movie.find('h3', class_="ipc-title__text").text.split('. ')[1]

        year = movie.find('span', class_="cli-title-metadata-item").text

        rating = movie.find('span', class_="ipc-rating-star").text.split('(')[0]

        print(rank, name, year, rating)
        

except Exception as e:
    print(e)