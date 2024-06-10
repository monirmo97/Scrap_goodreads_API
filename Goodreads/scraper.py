import requests
import re
from bs4 import BeautifulSoup
from .models import Book

def scrape_goodreads(query):
    base_url = "https://www.goodreads.com/search"
    for page in range(1, 6):
        params = {
            'page': page,
            'q': query,
            'qid': '68l8GEohzD',
            'search_type': 'books',
            'tab': 'books',
            'utf8': '✓'
        }
        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table with class "tableList"
        table_list = soup.find('table', class_='tableList')

        # Check if the tableList is found
        if table_list:
            # Find all rows <tr> with itemscope attribute
            rows = table_list.find_all('tr', attrs={'itemscope': True})
            
        for row in rows:
            title = row.find('a', class_='bookTitle').text.strip()
            author = row.find('a', class_='authorName').text.strip()

            # Find the minirating span
            minirating_span = row.find('span', class_='minirating')
            
            if minirating_span:
                # Splitting text to get average_rating and total_ratings
                minirating_text = minirating_span.text.split('—')
                # Extracting only the numeric part of average_rating
                average_rating_text = re.search(r'\d+\.\d+', minirating_text[0])
                average_rating = float(average_rating_text.group()) if average_rating_text else None
        
                # Extracting only the numeric part of total_ratings
                total_ratings_texts = re.findall(r'\d+', minirating_text[1])
                total_ratings = int(''.join(total_ratings_texts)) if total_ratings_texts else None
            else:
                average_rating = None
                total_ratings = None
                
            # Extracting edition_number from the link containing 'editions'
            editions_link = row.find('a', class_='greyText', href=lambda x: x and 'editions' in x)
            edition_number_text = re.search(r'\d+', editions_link.text)
            edition_number = int(edition_number_text.group()) if edition_number_text else None
            
            # Extracting numeric part of publish_year using regular expression
            publish_year_tag = row.find('span', class_='greyText smallText uitext')
            publish_year_text = re.search(r'\b\d{4}\b', publish_year_tag.text.strip())
            publish_year = int(publish_year_text.group()) if publish_year_text else None

            Book.objects.create(
                title=title,
                author=author,
                average_rating=average_rating,
                total_ratings=total_ratings,
                edition_number=edition_number,
                publish_year=publish_year
            )
