from django.shortcuts import render
from django.utils import timezone
from django.views import View

from .models import TagTitles
from video.models import VideoContent


class HomeView(View):
    def get(self, request):
        tag_names = TagTitles.objects.filter(title__icontains='a')
        videos = VideoContent.objects.filter().order_by('-created_at')

        for video in videos:
            video.days_ago = max(0, (timezone.now() - video.created_at).days)


        return render(request, 'home.html', {
            'top_button_names': tag_names,
            'videos': videos,
        })
