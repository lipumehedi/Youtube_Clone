from django.shortcuts import render

from django.views import View
from .models import TagTitles
from video.models import VideoContent

class HomeView(View):
    def get(self, request):
        tag_names = TagTitles.objects.filter(title__icontains='a')
        videos = VideoContent.objects.all().order_by('uploaded_at')
        return render(request, 'home.html', {'tag_names': tag_names, 'videos': videos})