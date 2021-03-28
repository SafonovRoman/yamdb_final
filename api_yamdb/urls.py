from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('titles.urls')),
    path('api/', include('yambd_auth.urls')),
    path('api/', include('opinions.urls')),
    path('redoc/',
         TemplateView.as_view(template_name='redoc.html'),
         name='redoc'),
]
