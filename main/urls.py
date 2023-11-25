from django.contrib import admin
from django.urls import path, include
from .views import main_page_view

# main_page/...
urlpatterns = [
    path('', main_page_view, name='main_page')
]
