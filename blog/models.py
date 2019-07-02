from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    comment = models.TextField()

    def __str__(self):
        return self.title
