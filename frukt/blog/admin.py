from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('title', 'status', 'slug', 'meta_tags', 'keywords')
    list_filter = ('status',)
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)

# admin.site.register(Post)
