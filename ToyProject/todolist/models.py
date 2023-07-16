from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    checked = models.BooleanField(default=False)
    
    def __str__(self):
        return self.content