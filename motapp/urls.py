from django.urls import path, include
from rest_framework import routers
from .views import AdvantagesViewset, Recommend_usViewset, HelpViewset, TariffViewset, ReviewViewset, IntegrationViewset, OpportunityViewset

# Advantages, Recommend_us, Help, Tariff, Review, Integration, Opportunity

router = routers.DefaultRouter()
router.register(r'advantage', AdvantagesViewset),
router.register(r'review', ReviewViewset),
router.register(r'help', HelpViewset),
router.register(r'tariff', TariffViewset),
router.register(r'recommend', Recommend_usViewset),
router.register(r'intergration', IntegrationViewset),
router.register(r'opportunity', OpportunityViewset),


urlpatterns = [
    path('', include(router.urls)),
    # path('tariff-api/', TariffsApiListview.as_view()),
    # path('tariff-api/', TariffsViewset.as_view()),
]