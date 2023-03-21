from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post


class StaticViewSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ['blog-home', 'blog-about', 'side-calendar', 'side-faq']

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.date_posted
