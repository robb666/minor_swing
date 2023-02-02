from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Post


# Register your models here.
class PostAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('page_title', 'slug', 'date_posted', 'description', 'status', 'order')
    list_filter = ('status',)
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)

# admin.site.register(Post)
