from  rest_framework import generics
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

from . import serializers
from django.shortcuts import render

from .models import Product


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = StandardResultsSetPagination
#     filter_
