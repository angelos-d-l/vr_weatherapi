from rest_framework import generics
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime
from operator import itemgetter


@api_view(['GET'])
def get_weather(self, field, city, date, time):
    print("field: ", field,
    "\n city: ", city,
    "\n date: ", date,
    "\n time: ", time
        )
    try:
        response = requests.get(
            'http://api.openweathermap.org/data/2.5/forecast',
            params=[('q', city), ('appid', '7b9d881fe7ce907fa92f73266a937fdf')]
            )
    except HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except Exception as err:
        print(f'Unknown Error: {err}')
    result = response.json()
    if result['message'] == "city not found":
        return Response({"message": "city not found", "status": "error"})
    date_list = []
    for d in result['list']:
        date_list.append(d['dt'])
    date_list.sort()
    timestamp = datetime.datetime(int(date[:4]), int(date[4:6]), int(date[6:]),
    int(time[:2]), int(time[2:]), tzinfo=datetime.timezone.utc).timestamp()
    if timestamp < date_list[0] or timestamp > date_list[-1]:
        return Response({"message": "Can not get forecasts further out than 5 days", "status": "error"})
    diff_list = [abs(variable - timestamp) for variable in date_list]
    closest_time = date_list[min(enumerate(diff_list), key=itemgetter(1))[0]]
    if field == "summary":
        for data in result['list']:
            if data['dt'] == closest_time:
                temp = round(data['main']['temp'] - 273.16)
                description = data['weather'][0]['description']
                humidity = data['main']['humidity']
                pressure = data['main']['pressure']
                return Response({"description": description,
                "humidity": {"unit": "%", "value": humidity},
                "pressure": {"unit": "hPa", "value": pressure},
                "temperature": {"unit": "C", "value": temp},
                "status": "success", "timestamp": data['dt_txt']
                })
    if field == "temperature":
        for data in result['list']:
            if data['dt'] == closest_time:
                temp = round(data['main']['temp'] - 273.16)
                return Response({
                "value": temp, "unit": "C",
                "status": "success", "timestamp": data['dt_txt']
                })
    if field == "humidity":
        for data in result['list']:
            if data['dt'] == closest_time:
                humidity = data['main']['humidity']
                return Response({
                "value": humidity, "unit": "%",
                "status": "success", "timestamp": data['dt_txt']
                })
    if field == "pressure":
        for data in result['list']:
            if data['dt'] == closest_time:
                pressure = data['main']['pressure']
                return Response({
                "value": pressure, "unit": "hPa",
                "status": "success", "timestamp": data['dt_txt']
                })
    return Response({"status": "error", "message":"unknown field"})
