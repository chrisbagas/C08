from django.contrib import admin



# Register your models here.

from forum.models import Comment, Forum



admin.site.register(Forum)
admin.site.register(Comment)