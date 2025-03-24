from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer, TaskCreateSerializer, TaskAssignSerializer
from users.models import User

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return TaskCreateSerializer
        return TaskSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    def assign(self, request, pk=None):
        task = self.get_object()
        serializer = TaskAssignSerializer(data=request.data)
        
        if serializer.is_valid():
            user_ids = serializer.validated_data['user_ids']
            users = User.objects.filter(id__in=user_ids)
            
            if len(users) != len(user_ids):
                return Response(
                    {'error': 'Some users were not found'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            task.assigned_to.set(users)
            return Response(TaskSerializer(task).data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def user_tasks(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response(
                {'error': 'user_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = get_object_or_404(User, id=user_id)
        tasks = Task.objects.filter(assigned_to=user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
