from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default='')
    content = RichTextField(blank=True, null=True, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    status = models.IntegerField(choices=STATUS, default=1)

    slug = models.SlugField(max_length=200, unique=True, default='')
    page_title = models.CharField(max_length=60, blank=True, null=True, default='')
    meta_tags = models.CharField(max_length=60, blank=True, null=True, default='')
    keywords = models.CharField(max_length=60, blank=True, null=True, default='')
    description = models.TextField(max_length=160, blank=True, null=True, default='')
    head = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return self.title

    # def __str__(self):
    #     return f'{self.user}'

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
