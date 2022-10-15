from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django import forms



# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


def about(request):
    image = Post.objects.get(id=33)
    # context = {
    #     'image': Post.objects.get(id=33)
    # }


    return render(request, 'blog/about.html', {'image': image})
