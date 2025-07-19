from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponseNotFound

urlpatterns = [

    path('admin/',admin.site.urls),
    #url para ocultar el admin
    #path('notUser/', admin.site.urls),
    #path('admin/', lambda request: HttpResponseNotFound("Not found.")),
    path('', include('users.urls')),
    path('', include('blog.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root =settings.STATIC_ROOT)
