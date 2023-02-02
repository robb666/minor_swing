from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    page_title = models.CharField(max_length=60, default='')
    slug = models.SlugField(max_length=60, unique=True, default='')
    description = models.TextField(max_length=160, blank=True, null=True, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    content = RichTextField(blank=True, null=True, default='')  # --> header? richTextField
    image = models.ImageField(null=True, blank=True, upload_to='blog_images')
    status = models.IntegerField(choices=STATUS, default=1)
    order = models.PositiveIntegerField(default=0, null=False)

    def __str__(self):
        return self.page_title

    class Meta:
        ordering = ['order']

    # def __str__(self):
    #     return f'{self.user}'

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
