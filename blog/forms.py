from django import forms
from .models import Comment

# CommentForm inherites from Django's forms.ModelForm class
class CommentForm(forms.ModelForm):
    # we can simply use the Meta class to tell the ModelForm class what models 
    # and fields we want in our form. form.ModelForm will then build this for us
    class Meta:
        model = Comment
        # We don't need to include the other fields because the post, user and 
        # created_on fields in our model are filled in automatically, and the 
        # approved field is managed by the superuser.
        fields = ('body',) 