from django.shortcuts import render
from .models import Advantages, Recommend_us, Help, Tariff, Review, Integration, Opportunity
from .serialayzer import AdvantagesSerializer, Recommend_usSerializer, HelpSerializer, TariffSerializer, ReviewSerializer, IntegrationSerializer, OpportunitySerializer #, AdvantagesApiSerializer, Recommend_usApiSerializer, HelpApiSerializer, TariffApiSerializer, ReviewApiSerializer, IntegrationApiSerializer, OpportunityApiSerializer

from rest_framework.response import Response
from rest_framework import viewsets, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView, ListAPIView

# Create your views here.

# Advantages, Recommend_us, Help, Tariff, Review, Integration, Opportunity


class AdvantagesViewset(viewsets.ModelViewSet):
    queryset = Advantages.objects.filter(status=True)
    serializer_class = AdvantagesSerializer
    permission_classes = [AllowAny]

class Recommend_usViewset(viewsets.ModelViewSet):
    queryset = Recommend_us.objects.filter(status=True)
    serializer_class = Recommend_usSerializer
    permission_classes = [AllowAny]

class HelpViewset(viewsets.ModelViewSet):
    queryset = Help.objects.filter(status=True)
    serializer_class = HelpSerializer
    permission_classes = [AllowAny]

class TariffViewset(viewsets.ModelViewSet):
    queryset = Tariff.objects.filter(status=True)
    serializer_class = TariffSerializer
    permission_classes = [AllowAny]

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.filter(status=True)
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

class IntegrationViewset(viewsets.ModelViewSet):
    queryset = Integration.objects.filter(status=True)
    serializer_class = IntegrationSerializer
    permission_classes = [AllowAny]

class OpportunityViewset(viewsets.ModelViewSet):
    queryset = Opportunity.objects.filter(status=True)
    serializer_class = OpportunitySerializer
    permission_classes = [AllowAny]















""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Advantages, Recommend_us, Help, Tariff, Review, Integration, Opportunity

# class AdvantagesApiDetailview(RetrieveAPIView):
#     queryset = Advantages.objects.filter(status=True)
#     serializer_class = AdvantagesApiSerializer
#     permission_classes = [AllowAny]
#     lookup_field = 'slug'

# class Recommend_usApiDetailview(RetrieveAPIView):
#     queryset = Recommend_us.objects.filter(status=True)
#     serializer_class = Recommend_usApiSerializer
#     permission_classes = [AllowAny]
#     lookup_field = 'slug'

# class HelpApiDetailview(RetrieveAPIView):
#     queryset = Help.objects.filter(status=True)
#     serializer_class = HelpApiSerializer
#     permission_classes = [AllowAny]
#     lookup_field = 'slug'

# class TariffApiDetailview(RetrieveAPIView):
#     queryset = Tariff.objects.filter(status=True)
#     serializer_class = TariffApiSerializer
#     permission_classes = [AllowAny]
#     lookup_field = 'slug'

# class ReviewApiDetailview(RetrieveAPIView):
#     queryset = Review.objects.filter(status=True)
#     serializer_class = ReviewApiSerializer
#     permission_classes = [AllowAny]
#     lookup_field = 'slug'

# class IntegrationApiDetailview(RetrieveAPIView):
#     queryset = Integration.objects.filter(status=True)
#     serializer_class = IntegrationApiSerializer
#     permission_classes = [AllowAny]
#     lookup_field = 'slug'

# class OpportunityApiDetailview(RetrieveAPIView):
#     queryset = Opportunity.objects.filter(status=True)
#     serializer_class = OpportunityApiSerializer
#     permission_classes = [AllowAny]
#     lookup_field = 'slug'













""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Advantages, Recommend_us, Help, Tariff, Review, Integration, Opportunity



# class AdvantagesApiListview(ListAPIView):
#     queryset = Advantages.objects.filter(status=True)
#     serializer_class = AdvantagesApiSerializer
#     permission_classes = [AllowAny]

# class Recommend_usApiListview(ListAPIView):
#     queryset = Recommend_us.objects.filter(status=True)
#     serializer_class = Recommend_usApiSerializer
#     permission_classes = [AllowAny]

# class HelpApiListview(ListAPIView):
#     queryset = Help.objects.filter(status=True)
#     serializer_class = HelpApiSerializer
#     permission_classes = [AllowAny]

# class TariffApiListview(ListAPIView):
#     queryset = Tariff.objects.filter(status=True)
#     serializer_class = TariffApiSerializer
#     permission_classes = [AllowAny]

# class ReviewApiListview(ListAPIView):
#     queryset = Review.objects.filter(status=True)
#     serializer_class = ReviewApiSerializer
#     permission_classes = [AllowAny]

# class IntegrationApiListview(ListAPIView):
#     queryset = Integration.objects.filter(status=True)
#     serializer_class = IntegrationApiSerializer
#     permission_classes = [AllowAny]

# class OpportunityApiListview(ListAPIView):
#     queryset = Opportunity.objects.filter(status=True)
#     serializer_class = OpportunityApiSerializer
#     permission_classes = [AllowAny]


