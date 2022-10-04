from django.db import models


class Product(models.Model):
    name = models.CharField("Название", max_length=250)
    price = models.IntegerField("Цена", default=0)
    description = models.CharField("Описание товара", max_length=500, null=True)
