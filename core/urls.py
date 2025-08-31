from django.urls import path, include
from . import views
from core.views import home



urlpatterns = [
    path('', home, name='home'),
]



urlpatterns = [
    path('', views.home, name='home'),
    path('send-message/', views.send_message, name='send_message'),
]
