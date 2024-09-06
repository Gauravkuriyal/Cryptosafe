from django.db import models


# Create your models here.
class user_data(models.Model):
    user_id = models.CharField(max_length=20,default=1001,null = False)
    encrypted = models.TextField(default = None,null = False)
    mail_id = models.EmailField(default=None, null= False , max_length = 320)
    date_time = models.DateTimeField(null=True)
    wrong_count = models.IntegerField(default = 0, null= False)

class current_id_no(models.Model):
    ref_id = models.PositiveIntegerField()

class feedback(models.Model):
    name = models.CharField(max_length=40,default="user",null= False)
    Address = models.TextField(default=None,null=False)
    email = models.EmailField(default=None, null= False , max_length = 320)
    country = models.CharField(max_length=10,default="India",null = False)
    feedback = models.TextField(default=None,null = False)
    date_time = models.DateTimeField(null=True)