from django.db import models
import os
# Create your models here.


def rename(instance,filename):
    upload_to = "static/imguploaded"
    ext = filename.split('.')[-1]
    if instance.name:
        filename = '{}.{}'.format(instance.name,ext)
    else:
        filename  = filename
    return os.path.join(upload_to,filename)
class Sample(models.Model):
    name= models.CharField(max_length=100,null=True)
    email = models.EmailField()
    img = models.ImageField(upload_to=rename)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=100,null=True)
    radio = models.BooleanField(null=True)
    # birthday = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    




