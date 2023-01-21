from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, SearchBar
from . import views
from contact.views import index

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('search/', SearchBar.as_view(), name='blog-search'),
    path('about/', views.about, name='blog-about'),
    path('contact/', index, name='form-contact'),
    path('harvest_calendar/', views.calendar, name='side-calendar'),
    path('faq/', views.faq, name='side-faq'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,)
