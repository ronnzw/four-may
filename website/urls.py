from . import views
from django.urls import path


app_name = 'website'
urlpatterns = [
    path('',views.home, name='home'),
    path('selectcurrency', views.select_currency, name="selectcurrency"),
    path('privacy', views.privacy, name='privacy'),
    path('terms', views.terms_of_use, name='terms')
]
    