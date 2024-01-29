from django.contrib import admin

# Register your models here.
from .models import Post

# we are registering the Post app in our admin site
admin.site.register(Post)