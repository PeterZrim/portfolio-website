import os
import json
import requests
from datetime import datetime, timedelta
import pytz
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import GalleryImage

def get_crypto_data():
    """Fetch cryptocurrency data from CoinGecko API"""
    try:
        # Get current prices
        coins = ['bitcoin', 'ethereum', 'dogecoin']
        prices_url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies=chf&include_24hr_change=true"
        prices_response = requests.get(prices_url, timeout=10)
        if prices_response.status_code != 200:
            print(f"Error fetching crypto prices: {prices_response.status_code}")
            return None
        prices_data = prices_response.json()

        # Get historical data for charts
        crypto_data = {}
        for coin in coins:
            try:
                # Get 24h historical data
                chart_url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=chf&days=1&interval=hourly"
                chart_response = requests.get(chart_url, timeout=10)
                if chart_response.status_code != 200:
                    print(f"Error fetching chart data for {coin}: {chart_response.status_code}")
                    continue
                chart_data = chart_response.json()['prices']

                crypto_data[coin] = {
                    'price': prices_data[coin]['chf'],
                    'change_24h': prices_data[coin]['chf_24h_change'],
                    'chart_data': chart_data
                }
            except Exception as e:
                print(f"Error processing {coin} data: {e}")
                continue

        return crypto_data if crypto_data else None
    except Exception as e:
        print(f"Error in get_crypto_data: {e}")
        return None

def get_weather_data():
    """Fetch weather data from OpenWeatherMap API"""
    try:
        api_key = os.getenv('OPENWEATHER_API_KEY')
        if not api_key:
            print("No OpenWeather API key found")
            return None
            
        city = "Zurich"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url, timeout=10)
        print(f"Weather API response status: {response.status_code}")
        
        if response.status_code != 200:
            print(f"Weather API error: {response.text}")
            return None
            
        data = response.json()
        print(f"Weather data received: {data}")
        
        weather_data = {
            'city': city,
            'temperature': round(data['main']['temp']),
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather_data
    except Exception as e:
        print(f"Error in get_weather_data: {str(e)}")
        return None

def get_image_files():
    """Get list of image files from the images directory"""
    images_dir = os.path.join(settings.BASE_DIR, 'main', 'static', 'main', 'images')
    image_files = []
    if os.path.exists(images_dir):
        for file in os.listdir(images_dir):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_files.append(file)
    image_files.sort()
    return image_files

class BaseContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) if hasattr(super(), 'get_context_data') else {}
        context['gallery_images'] = GalleryImage.objects.all().order_by('?')[:5]  # Random 5 images
        return context

def home(request):
    """Home page view"""
    context = {
        'crypto_data': get_crypto_data(),
        'weather_data': get_weather_data(),
        'images': get_image_files()
    }
    return render(request, 'main/home.html', context)

def about(request):
    """About page view"""
    context = {
        'images': get_image_files()
    }
    return render(request, 'main/about.html', context)

def programming(request):
    """Programming portfolio page view"""
    context = {
        'images': get_image_files()
    }
    return render(request, 'main/programming.html', context)

def music(request):
    """Music portfolio page view"""
    context = {
        'images': get_image_files()
    }
    return render(request, 'main/music.html', context)

def gallery(request):
    """Gallery page view"""
    return render(request, 'main/gallery.html', {'images': get_image_files()})
