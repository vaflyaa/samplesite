from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )

    fio = models.CharField('ФИО', max_length=255, default='')
    gender = models.CharField('Пол', max_length=1, choices=GENDER, default='')
    birth_date = models.DateField('Дата рождения', default='2000-09-12')
