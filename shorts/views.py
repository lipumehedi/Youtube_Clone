from django.shortcuts import render
from django.views import View


class ShortsView(View):
    def get(self, request):
        return render(request, 'shorts.html')


class ShortsWatchView(View):
    def get(self, request):
        return render(request, 'watch.html')


class MusicView(View):
    def get(self, request):
        return render(request, 'music.html')
