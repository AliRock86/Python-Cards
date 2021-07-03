from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    name_ar = models.CharField(max_length=100,unique=True)
    icon = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to="image_category",default=None)


class Sub_Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    name_ar = models.CharField(max_length=100,unique=True)
    icon = models.CharField(max_length=100,unique=True)
    category_id = models.ForeignKey(Category,related_name='sub_categories',on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image_sub_category",default=None)

class Status_Type(models.Model):
    name_type = models.CharField(max_length=20,unique=True)

class Status(models.Model):
    name = models.CharField(max_length=100,unique=True)
    name_ar = models.CharField(max_length=100,unique=True)
    status_type_id = models.ForeignKey(Status_Type,related_name='statuses',on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=100,unique=True)
    price = models.IntegerField(max_length=200)
    number = models.IntegerField(max_length=200,default=1)
    description = models.TextField(max_length=2000,default=None)
    image = models.ImageField(upload_to="image_item",default=None)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



