from django.urls import path,include
from .views import *

app_name = 'core'

urlpatterns = [
  
    path('', index, name='index'),
    path('index/<slug>/', index_detail, name='index_detail'),
    path('create/', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('subscribe',subscribe,name='subscribe'),
]