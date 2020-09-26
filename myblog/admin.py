from django.contrib import admin
from myblog.models import Contact
from myblog.models import Post

# Register your models here.
admin.site.register(Contact),
admin.site.register(Post)
