from music.views import addMusic, homePage, Music
from django.urls import path

app_name='musics'

urlpatterns = [
    path('',homePage,name='home_page'), 
    path('add/',addMusic,name='add_music'),  
]