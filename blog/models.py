from django.db import models
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=60)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images/blog")
    body = RichTextField(blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

    class Meta:
        ordering = ['-date_published']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def natural_key(self):
        return self.author

    def __str__(self):
        return self.title
