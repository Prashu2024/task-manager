from rest_framework import serializers
from .models import Task
from users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'task_type', 'status', 'assigned_to', 
                 'created_by', 'created_at', 'updated_at', 'completed_at')
        read_only_fields = ('created_at', 'updated_at', 'completed_at')

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'task_type', 'status')

class TaskAssignSerializer(serializers.Serializer):
    user_ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False
    ) 