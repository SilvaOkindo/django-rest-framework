from django.contrib import admin
from django.urls import path, include
from product_reviews.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]