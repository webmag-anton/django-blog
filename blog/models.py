from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # The cascade on delete means that on the deletion of the user entry, all their posts are also deleted.
    # The current model, Post, is connected to the User model, as User has been added to the ForeignKey field type as an argument.
    # A semantic related_name blog_posts is better than the default author_set from Django; it's an optional attribute used to give 
    # a meaningful name to the relation between two models.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    # The auto_now_add=True means the default created time is the time of post entry.
    # There is no Created on date picker input as we added the option auto_now_add=True
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    # The Meta class provides additional information or metadata about the model. Adding a class Meta is completely optional
    class Meta:
        ordering = ["-created_on"]  #  - symbol indicates descending order for a field
    # Methods should always be below Meta classes.
    # __str__ provides a human-readable representation of the model instance
    def __str__(self):
        return f"{self.title} | written by {self.author}"    


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"    