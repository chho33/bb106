from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User',
        on_delete=models.CASCADE,
        null=False)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
