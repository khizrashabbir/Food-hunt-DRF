from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status, generics, permissions
from rest_framework import filters
from .serializers import *
# Create your views here.


class MenuView(viewsets.ModelViewSet):
    serializer_class = MenuPicSerializer
    queryset = MenuPicture.objects.all()


class BookTableView(generics.ListCreateAPIView):
    search_fields = ['email', 'NoOfGuest', 'time', 'date']
    filter_backends = (filters.SearchFilter,)
    queryset = BookTable.objects.all()
    serializer_class = BookTableSerializer


class BlogView(viewsets.ModelViewSet):
    search_fields = ['category__category_name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = BlogSerializer
    queryset = FoodBlog.objects.all()


class Review(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()
