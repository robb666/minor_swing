from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return self.title

    # def __str__(self):
    #     return f'{self.user}'

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
