
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from diary import views

urlpatterns = [
    path('diary/', include('diary.urls')),
    path("", views.home),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
