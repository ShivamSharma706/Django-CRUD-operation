
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('', views.index_redirect, name='index_redirect'),
    path('web/', include('web.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  