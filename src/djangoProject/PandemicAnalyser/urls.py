from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name="index"), # /app
 path('registration/', views.register, name="register"), #/app/registration
 path('daily/', views.daily, name="daily"),
 path('models/', views.models, name="models"),
 path('keydates/', views.keydates, name="keydates"),
 path('about/', views.about, name="about")
]
