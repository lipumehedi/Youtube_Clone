from django.shortcuts import render
from django.views import View
from .models import TagTitles

class HomeView(View):
    def get(self, request):
        tag_names = TagTitles.objects.filter(title__icontains='a')
        return render(request, 'home.html', {'tag_names': tag_names})
