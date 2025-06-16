from django.urls import path

from .views import IndexView, base, SystemStatusAPIView, SystemStatusCpuAPIView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('base', base),
    path('api/system-status/', SystemStatusAPIView.as_view(), name='system-status'),
    path('api/system-status-cpu/', SystemStatusCpuAPIView.as_view(), name='system-status-cpu')
]