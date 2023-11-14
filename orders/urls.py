from django.urls import path

from orders.views import (OrderCreateView, OrderDetailView, OrderListView,
                          SuccessOrderView, my_webhook_handler)

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('success/', SuccessOrderView.as_view(), name='success_order'),
    path('checkout/', my_webhook_handler, name='checkout'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order'),
]
