from django.shortcuts import render

# init dash_app
from . import dash_app

def main_page_view(request):
    return render(request, 'index.html')
