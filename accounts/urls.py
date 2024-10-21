from . import views
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('profile/',views.profiles, name='profile'),
    path('dashboard', views.profile_dashboard, name='dashboard')
]