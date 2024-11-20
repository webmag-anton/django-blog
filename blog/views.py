from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
        # Django's generic views
class PostList(generic.ListView):
    # creates queryset (equal to  queryset = Post.objects.all())
    # model = Post     # returned all of the records from our Post model (all of the blog posts).   

    # queryset = Post.objects.filter(author=2)   /   Post.objects.all().order_by("-created_on")   /   Post.objects.filter(status=1)     
    queryset = Post.objects.all()      
    #  template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6    


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )    