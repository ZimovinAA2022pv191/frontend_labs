from django.db import models

from core.models.dicts import DictProduct


class Product(models.Model):
    name = models.CharField("Название", max_length=250)
    price = models.IntegerField("Цена", default=0)
    description = models.CharField("Описание товара", max_length=500, null=True)
    type_product = models.ForeignKey(DictProduct, on_delete=models.CASCADE)


class Image(models.Model):
    name = models.CharField("Имя", max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    path = models.ImageField(upload_to='media')
    date_upload = models.DateTimeField("Дата загрузки", auto_now=True)
