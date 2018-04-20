from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=120)
    body = models.CharField(max_length=120)
    createdAt = models.DateTimeField(auto_now=False,auto_now_add=True)



    def __str__(self):
        return self.title
