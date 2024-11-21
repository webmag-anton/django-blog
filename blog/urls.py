from . import views
from django.urls import path

urlpatterns = [
    # Django is looking for a URL that matches blog/ and then it will execute the PostList view from our views.py file.
    path('blog/', views.PostList.as_view(), name='home'),
    # <slug:slug> is where the slug value is passed from the template's URL tag.
    # This urlpattern (<slug:slug>) creates a url path of the domain path plus the slug value.
    #   The slug path converter before the colon defines the data type as a slug, 
    # and the slug after the colon is the post.slug value passed from the template. 
    # You see this value in the URL path in the browser bar.
    #   If you had a human resources web app that identified workers by 
    # their ID badge number, then you could use the syntax <int:id_badge>
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]