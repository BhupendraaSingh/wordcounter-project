
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('brand/', views.brand),
    path('about_this/', views.about, name = 'about'),
    path('counted/', views.count, name = 'count'),
    path('hi/', views.hi, name= 'hi')
]
