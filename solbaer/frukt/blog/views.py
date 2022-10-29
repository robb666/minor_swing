from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.db.models import Q
from django import forms


# # Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)



class PostListView(ListView):

    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=1)
    ordering = ['-date_posted']
    paginate_by = 2

    # TODO
    # def get_context_data(self, **kwargs):
    #     data = Post.objects.all()
    #     if 'query' in self.request.GET:
    #         q = self.request.GET['query']
    #         data = Post.objects.filter(Q(content__icontains=q))
    #     return render(self.request, 'blog/search.html', {'data': data})


class SearchBar(ListView):

    model = Post
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=1)
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('query')
        object_list = Post.objects.filter(Q(title__icontains=query) |
                                          Q(content__icontains=query))
        return object_list



# def searchbar(request):
#
#     query = request.GET.get('query')
#
#     if query and query != '':
#         results = Post.objects.filter(content__icontains=query)
#         print('success')
#     else:
#         results = Post.objects.filter(status=1)
#         results = results.date
#
#     context = {
#         'posts': results,
#     }
#     return render(request, 'blog/search.html', context)






class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


def about(request):
    image = Post.objects.get(id=35)
    # context = {
    #     'image': Post.objects.get(id=33)
    # }
    return render(request, 'blog/about.html', {'post': image})
