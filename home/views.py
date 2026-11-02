from django.shortcuts import render
from django.views import View
from .models import TagTitles

class HomeView(View):
    def get(self, request):
        tag_names = TagTitles.objects.all().exclude(title='Insects')
        return render(request, 'home.html', {'tag_names': tag_names})