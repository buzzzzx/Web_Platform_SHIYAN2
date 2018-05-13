from django.shortcuts import render


# Create your views here.

def index(requests):
    return render(requests, 'index.html')


def charts_test(requests):
    return render(requests, 'chart.html')


def temp_display(requests):
    return render(requests, 'tempchart.html')


def pressure_display(requests):
    return render(requests, 'preschart.html')


def gas_display(requests):
    return render(requests, 'gaschart.html')


def alarm(requests):
    return render(requests, 'alarmchart.html')


def log(requests):
    return render(requests, 'calendar.html')
