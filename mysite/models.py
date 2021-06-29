from django.db import models


# Create your models here.
class Product(models.Model):
    img = models.ImageField(upload_to='img/course_list', default='assets/images/product_03.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100, default="")
    desc = models.TextField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=200)
