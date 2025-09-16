from django.contrib import admin
from .models import Service, Master, Review, Order


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "duration", "is_popular"]
    list_filter = ["is_popular"]


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ["name", "experience", "is_active"]
    list_filter = ["is_active"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["client_name", "master", "rating", "created_at"]
    list_filter = ["rating", "created_at"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["client_name", "status", "appointment_date", "master"]
    list_filter = ["status", "master"]
