# WebScrapping-ImdbTopRatedMovies
>
> Scrapping the top rated movies data from IMDB website using Python(BeautifulSoup and Request module)

## Summary:  
  
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
=> open the VS-Code editor, make a file named 'scrapper.py'  
=> next, open the terminal in editor or cmd window and install the following modules:

    pip install request
    pip install bs4  
      
=> start to writing the code in 'scrapper.py'---   
--importing both the modules:

    import request
    from bs4 import BeautifulSoup  

=> now we are going to the google and type 'imdb top rated movies' on search bar--    
   open the website and copy the URL("https://www.imdb.com/chart/top/").