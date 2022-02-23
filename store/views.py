from itertools import product
from django.shortcuts import render
from rest_framework import generics
from .models import Products, Store
from .serializers import StoreSerializer,ProductSerializer
# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# ----------------------  Store Side -------------------

class Storelist(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store
    serializer_class = StoreSerializer

# ----------------------  Products Side -------------------

class getproduct(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StoreSerializer
    def get(self, request , pk , format = None):
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class getproduct1(GenericAPIView):

    def get(self,request,format=None):
        product = Products.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

class postproduct(GenericAPIView):
    serializer_class = StoreSerializer
    def post(self, request, format= None):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'message' : 'Data Created Successfully'})

class putproduct(GenericAPIView):
    serializer_class = StoreSerializer
    def put(self , request , pk = None , format = None):
        id = request.data.get('id')
        product = Products.objects.get(pk=id)
        serializer = ProductSerializer(product , data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'message' : 'Data Updated Successfully'})

class deleteproduct(GenericAPIView):
    serializer_class = StoreSerializer
    def delete(self, request, pk=None , format = None):
        id = request.data.get('id')
        product = Products.objects.get(pk=id)
        product.delete()
        return Response({'message' : 'Data Delete Sucessfully'})


    

