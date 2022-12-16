from django.db import models

# Create your models here.
class Registration(models.Model):
    uid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=120)
    phno=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name
   
