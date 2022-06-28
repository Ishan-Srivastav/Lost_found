from django.urls import path
from .views import lostpost
from . import views

app_name = 'LandF'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('Lost_Form/',lostpost, name='form')
]
