from django.contrib.auth.models import User  # Импорт модели пользователя Django
from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product)

    class Meta:
        db_table = 'Lesson'  # Указываем новое название таблицы
        verbose_name = 'Уроки'
        verbose_name_plural = 'Уроки'


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time_secons = models.IntegerField()
    is_completed = models.BooleanField(default=False)
