from django.urls import path
from .views import scrape_and_save

urlpatterns = [
    path('scrape/<str:query>/', scrape_and_save, name='scrape_and_save_with_query'),
]
