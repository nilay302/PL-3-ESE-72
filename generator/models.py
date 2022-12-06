from django.db import models

# Create your models here.
class Bonafide(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, null=True)
    Class = models.CharField(max_length=10, null=True)
    Year = models.CharField(max_length=5, null=True)
    reason = models.TextField(null=False ,default='Reason')
    created = models.DateTimeField(auto_now_add=True)