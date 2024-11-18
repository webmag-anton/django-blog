from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
        # Django's generic views
class PostList(generic.ListView):
    # creates queryset (equal to  queryset = Post.objects.all())
    # model = Post     # returned all of the records from our Post model (all of the blog posts).   

    # queryset = Post.objects.filter(author=2)   /   Post.objects.all().order_by("-created_on")   /   Post.objects.filter(status=1)     
    queryset = Post.objects.all()      
    template_name = "post_list.html"