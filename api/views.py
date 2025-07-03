from django.shortcuts import get_object_or_404
from api.seriializers import ProductSerializzer
from api.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializzer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializzer(product)
    return Response(serializer.data)