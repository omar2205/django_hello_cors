from django.urls import path
from front import views

urlpatterns = [
    path('', views.home),
    path('api', views.api)
]