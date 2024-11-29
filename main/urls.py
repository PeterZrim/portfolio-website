from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programming/', views.programming, name='programming'),
    path('music/', views.music, name='music'),
    path('gallery/', views.gallery, name='gallery'),
    path('get_weather/', views.get_weather_view, name='get_weather'),
]
