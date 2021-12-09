from django.contrib import admin
from django.urls.conf import path
from . import views


urlpatterns = [
    path('',views.index)
]