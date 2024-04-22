from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=50)
    task = models.CharField(max_length=50)
    date = models.DateField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title + " - " + self.task