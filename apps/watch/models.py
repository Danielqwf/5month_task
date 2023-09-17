from django.db import models
from django.core.validators import MinValueValidator

from apps.watch.constants import CONDITION_CHOICES, STYLE_CHOICES, GENDER_CHOICES, CASE_MATERIAL_CHOICES, COLOR_CHOICES, \
    STRAP_MATERIAL_CHOICES, CASE_SHAPE_CHOICES, WATER_RESISTANCE_CHOICES, MOVEMENT_CHOICES, GLASS_CHOICES


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
    glass = models.CharField(max_length=15, choices=GLASS_CHOICES, verbose_name='Стекло')
    case_material = models.CharField(max_length=100, choices=CASE_MATERIAL_CHOICES, verbose_name='Материал корпуса')
    dial_color = models.CharField(max_length=100, choices=COLOR_CHOICES, verbose_name='Цвет циферблата')
    band_color = models.CharField(max_length=100, choices=COLOR_CHOICES, verbose_name='Цвет ремешка/браслета')
    strap_material = models.CharField(max_length=100, choices=STRAP_MATERIAL_CHOICES,
                                      verbose_name='Материал ремешка/браслета')
    case_shape = models.CharField(max_length=100, choices=CASE_SHAPE_CHOICES, verbose_name='Форма корпуса')
    diameter = models.PositiveIntegerField(verbose_name='Диаметр корпуса (мм)')
    water_resistance = models.CharField(max_length=100, choices=WATER_RESISTANCE_CHOICES,
                                        verbose_name='Водонепроницаемость')
    movement = models.CharField(max_length=100, choices=MOVEMENT_CHOICES, verbose_name='Механизм')

    class Meta:
        verbose_name = 'Характеристикa'
        verbose_name_plural = 'Характеристики'