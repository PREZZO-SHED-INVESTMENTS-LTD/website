from django.urls import path
from brochure.views import CategoryListAPIView


urlpatterns = [
    path('brochures/', CategoryListAPIView.as_view(), name='category-list'),
]
