from rest_framework import serializers
from .models import Djangox

class DjangoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Djangox
        fields = ("id", "name", "description", "djangox_type")