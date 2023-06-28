from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.db.models import Q
from django.conf import settings
from django import forms


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=1)
    ordering = ['-date_posted']
    paginate_by = 3


class SearchBar(ListView):
    model = Post
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=1)
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Post.objects.filter(
                Q(page_title__icontains=query) |
                Q(content__icontains=query)).order_by('-date_posted')

            return object_list
        return ''


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        htp_rerefer = self.request.META.get('HTTP_REFERER')
        context['base_url'] = htp_rerefer if htp_rerefer else '/'

        return context


class PostCreateView(CreateView):
    model = Post
    fields = ['page_title', 'content']


def pricing(request):
    return render(request, 'blog/pricing.html')


def about(request):
    return render(request, 'blog/about.html')


def gallery(request):
    return render(request, 'blog/gallery.html')


def location(request):
    return render(request, 'blog/location.html', {'access_token': settings.MAPBOX_ACCESS_TOKEN})


def calendar(request):
    return render(request, 'blog/harvest_calendar.html')


def faq(request):
    return render(request, 'blog/FAQ.html')
