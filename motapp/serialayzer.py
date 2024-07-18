from .models import Advantages, Recommend_us, Help, Tariff, Review, Integration, Opportunity
from rest_framework import serializers


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Advantages
        fields = ('__all__')

class Recommend_usSerializer(serializers.ModelSerializer):
    class Meta:
        model= Recommend_us
        fields = ('__all__')

class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model= Help
        fields = ('__all__')

class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('__all__')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('__all__')

class IntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
        fields = ('__all__')

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ('__all__')










""" API """#Advantages, Recommend_us, Help, Tariff, Review, Integration, Opportunity

class AdvantagesApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = ('name', 'info')

class Recommend_usApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend_us
        fields = ('name',)

class HelpApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ('name', 'how')

class TariffApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('name', 'info', 'photo', 'video')

class ReviewApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('name', 'email', 'body', 'stars')

class IntegrationApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
        fields = ('name', 'info', 'photo', 'video')

class OpportunityApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ('name', 'about')