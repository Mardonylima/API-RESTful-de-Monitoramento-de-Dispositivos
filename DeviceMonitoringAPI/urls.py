from django.urls import path

from .views import IndexView, base

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('base', base),
]