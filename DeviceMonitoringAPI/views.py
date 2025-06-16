from django.shortcuts import render

from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services.system_monitor import collect_system_data
from .services.system_monitor import get_cpu_usage
from .serializers import SystemStatusSerializer, CpuUsageSerializer

# Create your views here.

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


def base(request):
    return render(request, 'base.html')


class SystemStatusAPIView(APIView):
    def get(self, request):
        system_data = collect_system_data()
        serializer = SystemStatusSerializer(system_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SystemStatusCpuAPIView(APIView):
    def get(self, request):
        cpu_usage = get_cpu_usage()
        serializer = CpuUsageSerializer({"cpu": cpu_usage})
        return Response(serializer.data, status=status.HTTP_200_OK)