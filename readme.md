# Django-Plotly-Dash
Django project with Plotly Dash



**install:**  
Create django project and move to root project folder.
- ``put data.csv to project folder``
- ``$ python3 -m venv venv``
- ``$ source venv/bin/activate``
- ``$ pip install -r requirements.txt``
- INSTALLED_APPS += 'django_plotly_dash.apps.DjangoPlotlyDashConfig'
- X_FRAME_OPTIONS = 'SAMEORIGIN'



to index.html file add:

``<div class="{% plotly_class name='dash_app' %} card" style="height: 100%; width: 100%;">
         {% plotly_app name='dash_app' ratio=1 %}
    </div>``

``$ python3 manage.py runserver``

open [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Deploed on Ubuntu Linux server with Gunicorn and Nginx. Link: [http://79.143.30.216/](http://79.143.30.216/)