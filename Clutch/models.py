from django.db import models
from django.contrib.postgres.fields import ArrayField

class UserManager(models.Manager):

    def logValidator(self, postData):
            errors = {}
            if postData['user_name'] != "setUserName" and postData['user_name'] != "adminUser":
                errors['user_name'] = "User name is invalid!"
            if postData['password'] != "setPassWord" and postData['password'] != "adminPassword":
                errors['password'] = "Password is invalid!"
            return errors

class User(models.Model):
    username = models.CharField(max_length=80, default="setUserName")
    password = models.CharField(max_length=80, default="setPassword")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()



class Items(models.Model):
    title = models.CharField(max_length= 80)
    description = models.CharField(max_length= 255)
    price = models.IntegerField(default=None)
    imgNums = ArrayField(models.IntegerField(default=None), size=None, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Image(models.Model):
    image = models.ImageField(upload_to='Image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)