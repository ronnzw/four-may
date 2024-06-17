from . import views
from django.urls import path
from .views import profiles


app_name = 'accounts'
urlpatterns = [
    path('',views.profiles, name='profile'),
]