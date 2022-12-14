from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Mobile(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    main_type=models.CharField(max_length=255)
    model_type=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    battary_size = models.IntegerField()
    colors = models.TextField(blank=True)
    price = models.IntegerField()
    def __str__(self):
        return self.main_type
    
class Post(models.Model):
    
    titel=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    
    def __str__(self):
        return self.titel