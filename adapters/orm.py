from django.db import models

# Create your models here.


class Tasks(models.Model):
    task = models.CharField(max_length=50)
    priority = models.IntegerField()
    userId = models.IntegerField()

    def __str__(self):
        return f"Task: {self.task} Priority: {self.priority}"
