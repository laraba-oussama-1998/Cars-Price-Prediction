from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import CarPrice
from .serializers import CarPriceSerializer
from rest_framework.views import APIView
from rest_framework import generics
from .ml_model.Load_model import load_model, prepare_data
# Create your views here.

class CarPriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarPrice.objects.all()
    serializer_class = CarPriceSerializer

class CarPriceList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        carprice = CarPrice.objects.all()
        serializer = CarPriceSerializer(carprice, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarPriceSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data.keys())
            data = prepare_data(serializer.validated_data)
            model = load_model(data)
            serializer.validated_data['price'] = round(model.predict(data)[0],2)
            print(serializer.validated_data)
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
@api_view(['GET', 'POST'])
def car_price(request):

    if request.method == 'GET':
        car_instances = CarPrice.objects.all()
        serializer = CarPriceSerializer()
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CarPriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
"""