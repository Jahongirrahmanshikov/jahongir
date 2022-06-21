from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

class Content(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    name = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    pubdate = models.DateField(default=0)
    link = models.FileField(default=0, upload_to='upload')
    status = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'