from django.db import models


# Create your models here.
class Product(models.Model):
    img = models.ImageField(upload_to='img/course_list', blank=True, null=True, default='assets/images/product_03.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=200, blank=True, null=True)
