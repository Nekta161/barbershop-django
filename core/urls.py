from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("orders/", views.orders_list, name="orders_list"),
    path("orders/<int:pk>/", views.order_detail, name="order_detail"),
    path("orders/create/", views.create_order, name="create_order"),
    path("review/create/", views.create_review, name="create_review"),
    path("thanks/", views.thanks, name="thanks"),
]
