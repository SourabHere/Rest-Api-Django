from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)
    product_Category=models.CharField(max_length=150,default="")
    product_brand_name=models.CharField(max_length=200,default="")
    product_img=models.ImageField(upload_to="prod/images",default="")

    def __str__(self):
        return self.product_name