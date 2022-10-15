from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views
from contact.views import index

# from django.conf import settings
# from django.conf.urls.static import static




urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
    path('contact/', index, name='form-contact')
]



# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
