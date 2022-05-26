from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item, Car
from .serializers import ItemSerializer, CarSerializer

@api_view(['GET']) #api view decorator
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET']) #api view decorator
def getData(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addCar(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)