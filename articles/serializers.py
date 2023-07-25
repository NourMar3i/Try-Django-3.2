from rest_framework import serializers
from .models import Article

# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item 
#         fields = ('__all__')

# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = ('__all__')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('__all__')