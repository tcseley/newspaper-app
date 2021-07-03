from django.db import models
from django.urls import reverse
from django.conf import settings  # we can use -> models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE
from django.contrib.auth import get_user_model # <- or this?



# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
