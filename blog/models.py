from pyexpat import model
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.title + ' (created ' + str(self.date) + ')'