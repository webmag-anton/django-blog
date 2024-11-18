from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin # enabling access to functionality in the admin panel for posts


@admin.register(Post)   # The decorator is how we register a class, compared to just registering the standard model as we did before
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.  (This will allow you to create, update and delete blog posts from the admin panel)
# admin.site.register(Post)     # we use decorator @admin.register(Post) instead
admin.site.register(Comment)