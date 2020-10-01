from django.urls import path

from . import views

app_name = "dictionary"

urlpatterns = [
    path('', views.index, name='index'),
    path('translation/<str:word>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]
