from django.db import models
from users.models import User

class Task(models.Model):
    TASK_TYPE_CHOICES = [
        ('FEATURE', 'Feature'),
        ('BUG', 'Bug'),
        ('DOCUMENTATION', 'Documentation'),
        ('MAINTENANCE', 'Maintenance'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    task_type = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tasks'
        ordering = ['-created_at']
