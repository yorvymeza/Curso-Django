from django.contrib import admin
from django.urls import path, include

from .views import HomeView

# from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomeView.as_view(), name='home')
]
