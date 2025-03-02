import stripe
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(["POST"])
def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": "AI PDF Pro Plan"},
                "unit_amount": 900,  # $9.00 in cents
            },
            "quantity": 1,
        }],
        success_url="https://yourdomain.com/success",
        cancel_url="https://yourdomain.com/cancel",
    )
    return Response({"sessionId": session.id})
