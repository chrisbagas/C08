from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'thumbnail', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'focus:ring-indigo-500 focus:border-indigo-500 flex-1 block rounded-md w-full border-gray-300', 'placeholder': 'Write the title for your blog post here.'}),
            'subtitle': forms.TextInput(attrs={'class': 'focus:ring-indigo-500 focus:border-indigo-500 flex-1 block rounded-md w-full border-gray-300', 'placeholder': 'Write an appealing subtitle for your blog post here.'}),
            'thumbnail': forms.FileInput(attrs={'class': 'mt-1 w-full flex justify-center rounded-md py-2 px-3 shadow-sm text-sm font-medium text-white bg-green-600'}),
            'body': forms.Textarea(attrs={'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full border border-gray-300 rounded-md', 'placeholder': 'Write your blog contents here.', 'rows': 16})
        }
