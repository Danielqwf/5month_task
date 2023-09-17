from django.db import models
from django.core.validators import MinValueValidator

from apps.watch.constants import CONDITION_CHOICES, STYLE_CHOICES, GENDER_CHOICES


class Watch(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=50, verbose_name='Модель')
    price = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Цена')
    country = models.CharField(max_length=50, verbose_name='Страна производитель')
    year = models.PositiveIntegerField(verbose_name='Год выпуска', validators=[MinValueValidator(1900)])
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'


class WatchCategory(models.Model):
    watch = models.OneToOneField(Watch, on_delete=models.CASCADE, verbose_name='Часы', related_name='category')
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, verbose_name='Пол')
    style = models.CharField(max_length=100, choices=STYLE_CHOICES, verbose_name='Стиль')
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=100, verbose_name='Состояние')


    class Meta:
        verbose_name = 'Характеристикa'
        verbose_name_plural = 'Характеристики'