from django.contrib import admin
from .models import Blog, Image, Video

admin.site.register(Video)
admin.site.register(Blog)
admin.site.register(Image)

admin.site.site_header = "ZUMBA WITH YASHI"