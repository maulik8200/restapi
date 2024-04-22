from rest_framework import serializers
from .models import *

class tasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'