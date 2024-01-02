# WebScrapping-ImdbTopRatedMovies
>
> Scrapping the top rated movies data from IMDB website using Python(BeautifulSoup and Request module)

### Summary:  
  
We are taken the data(top rated movies of 2023) from Imdb website and put it in the spreadsheet format.  
--------------We use Python for that-----------------  
    --using Modules:  
        1. Request module -- to get the URL request of website  
        2. BeautifulSoup module -- to fetch and store the data in Excel file.  
  
All the data contain inside the HTML tags of the website
    (which can be seen from the 'inspect' button by right-clicking on the website page).

------------

###### Let's get Started.....

=> first we have Python installed in our system.  
=> open the VS-Code editor, make a file named 'scrape.py'  
=> next, open the terminal in editor or cmd window and install the following modules:

    pip install request
    pip install bs4  
    pip install openpyxl
      
=> start to writing the code in 'scrape.py'---   
--importing both the modules:

    import request
    from bs4 import BeautifulSoup

=> now go to google and type 'imdb top rated movies' on search bar--    
   open the website and copy the URL("https://www.imdb.com/chart/top/").  

=> we need to configure our scrapper to **send a fake user-agent with every request**--  
--to prevent a website to block a web scraper and return a 403 error is because you are telling the website that you are a scraper in the **user-agents**, you send to the website when making your requests.  
for more details : [click here](https://scrapeops.io/web-scraping-playbook/403-forbidden-error-web-scraping/#use-fake-user-agents)

    user_agents_list = [
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]
    response = requests.get('https://www.imdb.com/chart/top/', headers={'User-Agent': random.choice(user_agents_list)})
    response.raise_for_status()

=> two more modules are also import as:

    #for fake user agents generation:
    import random

    #to save the data in excel sheet:use openpyxl
    import openpyxl

=> and then we scapped our useful data by writing some lines of code:

    data = BeautifulSoup(response.text, 'html.parser')

    movies = data.find('ul', class_="ipc-metadata-list").find_all('li', class_="ipc-metadata-list-summary-item")

    for movie in movies:

        rank = int(movie.find('h3', class_="ipc-title__text").text.split('. ')[0])
        name = movie.find('h3', class_="ipc-title__text").text.split('. ')[1]
        year = int(movie.find('span', class_="cli-title-metadata-item").text)
        rating = float(movie.find('span', class_="ipc-rating-star").text.split('(')[0])

        sheet.append([rank, name, year, rating])

=>  Finally we have the data in Excel Sheet named 'IMDB Movies Rating.xlsx'.  

### *END