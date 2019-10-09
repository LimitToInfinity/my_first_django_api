from rest_framework import serializers
from .models import HereWeGo

class HereWeGoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HereWeGo
        fields = ("id", "url", "name", "speed")