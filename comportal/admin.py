from django.contrib import admin

from comportal.models import Image
from .models import Complain, Post

admin.site.register(Complain)
admin.site.register(Post)
admin.site.register(Image)
