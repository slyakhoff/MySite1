from django.db import models

# Create your models here.
class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name="Пицерия")
    descr = models.TextField(verbose_name="Описание")
    rating = models.FloatField(default=0, verbose_name="Рейтинг")
    url = models.URLField(verbose_name="Интернет адрес пиццерии")
    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzashopKey = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="Пицца")
    descr = models.TextField(verbose_name="Описание")
    price = models.FloatField(default=0, verbose_name="Цена")
    def __str__(self):
        return self.name