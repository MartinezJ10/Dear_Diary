
from django.contrib import admin
from django.urls import include, path

from diary import views

urlpatterns = [
    path('diary/', include('diary.urls')),
    path("", views.home),
    path('admin/', admin.site.urls),
]
