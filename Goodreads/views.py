from django.http import JsonResponse
from .scraper import scrape_goodreads

def scrape_and_save(request, query):
    scrape_goodreads(query)
    return JsonResponse({'message': f'Data scraped and saved for query: {query}.'})
