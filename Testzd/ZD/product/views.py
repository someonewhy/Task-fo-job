from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lesson, Product
from .serializers import LessonViewSerializer, LessonSerializer
from django.db.models import Count, Sum, F, ExpressionWrapper, DecimalField
from django.db.models.functions import Coalesce

# Create your views here.

class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        return Lesson.objects.filter(products__owner=user)


class ProductLessonsView(generics.ListAPIView):
    serializer_class = LessonViewSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']  # Получаем id продукта из URL

        # Получить уроки, связанные с данным продуктом, и информацию о просмотре
        return Lesson.objects.filter(products__id=product_id, lessonview__user=user)

@api_view(['GET'])
def product_statistics(request):
    products = Product.objects.annotate(
        total_views=Count('lesson__lessonview'),
        total_view_time=Coalesce(Sum('lesson__lessonview__view_time_secons'), 0),
        total_students=Count('lesson__lessonview__user', distinct=True),
        purchase_percent=ExpressionWrapper(
            F('user__count') / F('total_students') * 100,
            output_field=DecimalField(max_digits=5, decimal_places=2)
        )
    )

    product_data = []
    for product in products:
        product_info = {
            'product_id': product.id,
            'product_name': product.name,
            'total_views': product.total_views,
            'total_view_time_seconds': product.total_view_time,
            'total_students': product.total_students,
            'purchase_percent': product.purchase_percent,
        }
        product_data.append(product_info)

    return Response(product_data)