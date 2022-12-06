from rest_framework.viewsets import ReadOnlyModelViewSet

from product_reviews.models import Product
from product_reviews.serializers import ProductSerializer


# Create your views here.


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
