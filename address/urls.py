from . import views
from django.urls import path


app_name = 'address'
urlpatterns = [
    path('',views.addres, name='addres'),
]