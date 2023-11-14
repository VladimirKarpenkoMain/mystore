import uuid

from django.conf import settings
from django.urls import reverse
from yookassa import Configuration, Payment

from products.models import Basket
from users.models import User

Configuration.account_id = settings.UKASSA_ID
Configuration.secret_key = settings.UKASSA_SECRET_KEY


def create_payment(order, request):
    user = User.objects.get(id=request.user.id)
    basket = Basket.objects.filter(user=user)
    description = f"Заказ для {request.POST.get('email')}"
    value = basket.total_sum()
    return_url = '{}{}'.format(settings.DOMAIN_NAME, reverse('orders:success_order'))

    payment = Payment.create({
        "amount": {
            "value": f"{value}",
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": return_url,
        },
        "metadata": {
            "order_id": order.id,
            "user_id": user.id
        },
        "capture": True,
        "refundable": False,
        "description": description
    }, uuid.uuid4())

    return payment
