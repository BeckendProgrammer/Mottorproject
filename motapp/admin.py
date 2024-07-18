from django.contrib import admin
from .models import Advantages, Recommend_us, Help, Tariff, Review, Integration, Opportunity
# Register your models here.

@admin.register(Advantages)
class AdvantagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'info','id', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'status', 'created_at')



@admin.register(Recommend_us)
class Recommend_usAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'status', 'created_at')



@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    list_display = ('name', 'how', 'id', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'status', 'created_at')



@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('name', 'info', 'photo', 'video', 'id', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'status', 'created_at')



@admin.register(Integration)
class IntegrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'info', 'photo', 'video', 'id', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'status', 'created_at')



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body', 'stars', 'id', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'status', 'created_at')



@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'status', 'created_at')