# vr_weatherapi

This is a simple weather forcast api
using openweather and django.


1. Installation.
    - virtualenv vr_weatherapi
    - cd vr_weatherapi
    - pip install django djangorestframework djangorestframework-jwt requests
    - source bin/activate
    - clone the repository
    - Go to the directory created
    - cd forecasts
    - python manage.py runserver

    Server should be availiable at 127.0.0.1:8000/

2. Usage:
    - Summary mode example:
        - http://127.0.0.1:8000/weather/summary/london/20190526/1800
    - Details mode example:
        - http://127.0.0.1:8000/weather/humidity/berlin/20190526/1800

3. Additional questions :

   - We could pass a parameter on the url for example unit_temp=Kelvin
   - Create module tests.py inside weather/api folder. Utilize rest_framework.test APITestCase
   after writting the tests run python manage.py test.
   - We should be able to provide an authentication method
   e.g.: generation of a jwt token for them to use.
   - Check error messages for non valid dates times and cities
   and success messages for valid requests..
   - DEFAULT_PERMISSION_CLASSES & DEFAULT_AUTHENTICATION_CLASSES of REST_FRAMEWORK inside forecasts/settings.py module should be specified.
   - We could write a script for bulk download of the data
   and populating a database with the data. This script could be
   called by crontab for example every six hours.