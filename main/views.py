from django.shortcuts import render

import functools
from . import dash_app


@functools.lru_cache(maxsize=None)
def init_dash_app_cached():
    return dash_app


def main_page_view(request):
    dash_app_instance = init_dash_app_cached()
    return render(request, 'index.html')

