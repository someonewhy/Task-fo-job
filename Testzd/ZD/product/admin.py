from django.contrib import admin

from .models import Lesson, Product


# Register your models here.
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_link', 'duration_seconds')
    search_fields = ('name',)  # Поиск по названию урока


admin.site.register(Lesson, LessonAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')  # Замените 'other_field' на дополнительные поля, которые вы хотите отображать


admin.site.register(Product, ProductAdmin)
