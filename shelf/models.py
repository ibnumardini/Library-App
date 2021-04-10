from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=500)
    writer = models.CharField(max_length=500)
    publisher = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='images/thumb/', null=True)
    amount = models.IntegerField(null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

