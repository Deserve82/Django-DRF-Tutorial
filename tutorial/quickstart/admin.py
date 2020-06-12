from django.contrib import admin
from .models import Poll, Choice, Post

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Post)
