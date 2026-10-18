
from django.urls import path
from .views import ShortsView, ShortsWatchView, MusicView

urlpatterns = [
    path('',ShortsView.as_view(), name='shorts'),
    path('watch/',ShortsWatchView.as_view(), name='watch'),
    path('watch/music/',MusicView.as_view(), name='music'),
]