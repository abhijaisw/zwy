from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from blog.views import gellary




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('gellary', gellary, name='Gellary'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
