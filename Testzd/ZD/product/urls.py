from django.urls import path
from . import views

urlpatterns = [
    path('lessons/', views.LessonListView.as_view(), name='lesson-list'),
    path('lesson-views/<int:product_id>/', views.ProductLessonsView.as_view(), name='lesson-view-list'),
    path('product-statistics/', views.product_statistics, name='product-statistics'),
]
