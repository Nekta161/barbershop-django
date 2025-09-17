from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Master, Review, Order
from django.db.models import Sum


def landing(request):
    masters = Master.objects.filter(is_active=True).prefetch_related("services")
    reviews = Review.objects.filter(is_published=True).select_related("master")
    return render(request, "landing.html", {"masters": masters, "reviews": reviews})


@login_required
def orders_list(request):
    query = request.GET.get("q", "")
    search_name = request.GET.get("search_name", "on")
    search_phone = request.GET.get("search_phone", "")
    search_comment = request.GET.get("search_comment", "")

    orders = (
        Order.objects.select_related("master")
        .prefetch_related("services")
        .order_by("-date_created")
    )

    q_objects = Q()
    if search_name == "on" and query:
        q_objects |= Q(client_name__icontains=query)
    if search_phone and query:
        q_objects |= Q(phone__icontains=query)
    if search_comment and query:
        q_objects |= Q(comment__icontains=query)

    if q_objects:
        orders = orders.filter(q_objects)

    return render(
        request,
        "orders_list.html",
        {
            "orders": orders,
            "query": query,
            "search_name": search_name,
            "search_phone": search_phone,
            "search_comment": search_comment,
        },
    )


@login_required
def order_detail(request, pk):
    order = (
        Order.objects.select_related("master")
        .prefetch_related("services")
        .annotate(total_price=Sum("services__price"))
        .get(pk=pk)
    )
    return render(request, "order_detail.html", {"order": order})
