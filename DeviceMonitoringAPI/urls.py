from django.urls import path

from .views import IndexView, base, SystemStatusAPIView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('base', base),
    path('api/system-status/', SystemStatusAPIView.as_view(), name='system-status'),
]