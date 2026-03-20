from django.db import models
from django.conf import settings
from client.models import Job


class JobApplication(models.Model):

    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status = models.CharField(max_length=20, default="Pending")

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.worker} applied for {self.job}"
