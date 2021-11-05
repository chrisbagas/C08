from django import forms
from django.forms import fields
from .models import Forum

# class ForumForm(forms.ModelForm):
#     class Meta:
#         model = Forum
#         fields = [
#             "title",
#             "body"
#         ]
#         """ 
#         title
#         author
#         body
#         time_created
#         time_modified 
#         """