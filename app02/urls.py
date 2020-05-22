from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('intelligence/',views.intelligence,name="intelligence"),
    path('home2/',views.home2,name="home2")

]