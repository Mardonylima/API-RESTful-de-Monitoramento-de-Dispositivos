from rest_framework import serializers


class SystemStatusSerializer(serializers.Serializer):
    cpu = serializers.FloatField()
    memory = serializers.DictField()
    disk = serializers.DictField()
    system_info = serializers.DictField()


class CpuUsageSerializer(serializers.Serializer):
    cpu = serializers.FloatField()
