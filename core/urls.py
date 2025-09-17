from django.urls import path
from . import views


urlpatterns = [
    path("", views.landing, name="landing"),
    path("orders/", views.orders_list, name="orders_list"),
    path("orders/<int:pk>/", views.order_detail, name="order_detail"),
]
