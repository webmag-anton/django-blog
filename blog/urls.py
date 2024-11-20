from . import views
from django.urls import path

urlpatterns = [
    # Django is looking for a URL that matches blog/ and then it will execute the PostList view from our views.py file.
    path('blog/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]