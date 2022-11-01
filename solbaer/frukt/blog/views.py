from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.db.models import Q
from django import forms


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=1)
    ordering = ['-date_posted']
    paginate_by = 2


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
                Q(title__icontains=query) |
                Q(content__icontains=query)).order_by('-date_posted')
            return object_list
        return ''


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


def about(request):
    image = 'https://django-frukt-files.s3.eu-west-1.amazonaws.com/images/sprz_d.jpg'
    # image = Post.objects.get(id=43)

    return render(request, 'blog/about.html', {'image': image})


def calendar(request):
    image = 'https://django-frukt-files.s3.eu-west-1.amazonaws.com/images/calendar.webp'
    # image = {
    #     'image': image
    # }
    return render(request, 'blog/harvest_calendar.html', {'image': image})
