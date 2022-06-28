from django.urls import path
from . import views

app_name = 'LandF'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/Lost_Form/',views.DetailView.as_view(), name='form')
]
