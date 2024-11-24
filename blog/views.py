from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


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


# this is a function-based view, no as_view() method is required. 
# A view function takes a web request and returns a web response.
# The slug parameter gets the argument value from the URL pattern named post_detail. (the slug value is unique)
def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        # The is_valid() method checks our model to see the constraints on our fields. For example, 
        # we discussed before that, the default behaviour in Django is that a field cannot be null. 
        # The is_valid() method makes sure we don't try to write a null value to the database.
        if comment_form.is_valid():
            # calling the save method with commit=False returns an object that 
            # hasn't yet been saved to the database so that we can modify it further (add author, ...).
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            # we can create messages in one request and use them in another (usually the next one).
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()
    print("About to render template")

    # The response our view is returning is the contents of a webpage containing one post.
    return render(
        request,
        "blog/post_detail.html",
        # Context - is how you pass data from your own views to a template.
        # Put simply, context is a Python dictionary of key/value pairs that is sent to the template.
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        }, # this context (a dictionary of data) is passed to the template
    )    


def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        # By specifying instance=comment, any changes made to the form 
        # will be applied to the existing Comment, instead of creating a new one.
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
    # HttpResponseRedirect is a Django class that tells the browser to go to a different URL.
    #   reverse is a Django function that constructs a URL from the provided URL path name and 
    # any relevant URL arguments: args=[slug].
    #   Using the slug argument ensures the user is returned to the same blog post on which they 
    # edited or deleted a comment.
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))    


def comment_delete(request, slug, comment_id):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))    