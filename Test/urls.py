from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views as v1
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.onLoad),
    path('login/',v1.login)
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

