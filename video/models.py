from django.db import models

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=255)
    logo = models.URLField()
    is_channel_verified = models.BooleanField(default=False)
    subscribers_count = models.IntegerField(default=0)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class VideoContent(models.Model):
    title = models.CharField(max_length=255)
    thumbnail_url = models.URLField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    views_count = models.IntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title