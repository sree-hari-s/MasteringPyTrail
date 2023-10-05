from django.shortcuts import render 
from django.http import HttpResponse
import pyowm

# Create your views here.
def index(request):
    return HttpResponse("Include name of the place '/place_name' in url.")

def rain(request, place_name):
    owm = pyowm.OWM('Your_Api_Key')
    manager = owm.weather_manager()

    try:
        observe = manager.weather_at_place(place_name)
    except pyowm.commons.exceptions.NotFoundError:
        return HttpResponse("Couldn't find the place")
    except pyowm.commons.exceptions.ConnectTimeoutError:
        return HttpResponse("Something went wrong")
    
    weather = observe.weather
    weather_status = weather.status

    return render(request, "rain_check.html", {
        "raincheck" : weather_status.lower() in ["rain", "drizzle", "thunderstrom"]
    })
    
