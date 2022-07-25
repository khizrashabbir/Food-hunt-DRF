from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status, generics, permissions
from rest_framework import filters
from .serializers import *
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
# Create your views here.

class GoogleLogin(SocialLoginView):
    authentication_classes = [] # disable authentication
    adapter_class = GoogleOAuth2Adapter
    # callback_url = "http://localhost:3000"
    client_class = OAuth2Client


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
