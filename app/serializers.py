from rest_framework import serializers
from .models import *


class MenuPicSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(MenuPicSerializer, self).__init__(many=many, *args, **kwargs)
    class Meta:
        url = ''
        model = MenuPicture
        fields = '__all__'


class BookTableSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(BookTableSerializer, self).__init__(many=many, *args, **kwargs)
    class Meta:
        url = ''
        model = BookTable
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(BlogSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        url=''
        model = FoodBlog
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(ReviewSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        url=''
        model = Reviews
        fields = '__all__'