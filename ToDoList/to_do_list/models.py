from django.db import models

# Create your models here.
class task(models.Model):
    task_name = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.task_name