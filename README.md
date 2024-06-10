# Goodreads Scraper
Goodreads Scraper is a Python project that scrapes and saves data from Goodreads, a popular website for book lovers. It allows users to search for books by keywords and get information such as title, author, average rating, total ratings, edition number, and publish year.

## Features
•  Scrapes data from Goodreads using requests and BeautifulSoup
•  Saves data in a SQLite database using Django models
•  Provides a web interface and an API for users to enter queries and get results
•  Displays the scraped data in a JSON format


## Installation
To install Goodreads Scraper, you need to have Python 3 and Django installed on your system. You can use pip to install Django:
pip install django==4.2
You also need to install requests and BeautifulSoup, which are external libraries for web scraping:
pip install requests
pip install beautifulsoup4
Then, you need to clone this repository or download the zip file and extract it. Navigate to the project directory and run the following commands to set up the database and start the server:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Usage
To use the API, you can send a GET request to the following endpoint:
•  GET http://127.0.0.1:8000/goodreads/scrape/keyword>/ to scrape and save data from Goodreads by keyword. You need to provide the keyword as a path parameter. 
