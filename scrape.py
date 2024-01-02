import requests
from bs4 import BeautifulSoup
import random
import openpyxl

#*****************************************************************************************************************************

#---creating a workbook in excel---
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Top Rated 250 Movies"
sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Rating'])

#*****************************************************************************************************************************

try:

    #------getting the Imdb URL request----
    user_agents_list = [
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
]
    response = requests.get('https://www.imdb.com/chart/top/', headers={'User-Agent': random.choice(user_agents_list)})
    response.raise_for_status()

    #---extracting whole data of URL in HTML format---
    data = BeautifulSoup(response.text, 'html.parser')

    #---find the tag contains our movies list and stored in 'movies'---
    movies = data.find('ul', class_="ipc-metadata-list").find_all('li', class_="ipc-metadata-list-summary-item")

    #---start a loop to find the info/column data we want, 
       #the info we want to scarpe contains in different tags with its class name provided--- 
    for movie in movies:

        rank = int(movie.find('h3', class_="ipc-title__text").text.split('. ')[0])
        name = movie.find('h3', class_="ipc-title__text").text.split('. ')[1]
        year = int(movie.find('span', class_="cli-title-metadata-item").text)
        rating = float(movie.find('span', class_="ipc-rating-star").text.split('(')[0])

        sheet.append([rank, name, year, rating])

except Exception as e:
    print(e)

#******************************************************************************************************************************

#--save the excel file--
excel.save('IMDB Movies Rating.xlsx')