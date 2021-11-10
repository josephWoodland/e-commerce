from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product

import json
import time


class StripWH_Handler:
    """
    Handle Stripe webhooks
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        # Clean the shipping detials
        for field, value in shipping_detials.address.items():
            if value == '':
                shipping_detials.address[field] = None

        order_exsist = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name_iexact=shipping_detials.name,
                    email_iexact=shipping_detials.email,
                    phone_number_iexact=shipping_detials.phone_number,
                    country_iexact=shipping_detials.country,
                    postcode_iexact=shipping_detials.postcode,
                    town_or_city_iexact=shipping_detials.town_or_city,
                    street_address1_iexact=shipping_detials.street_address1,
                    street_address2_iexact=shipping_detials.street_address2,
                    county_iexact=shipping_detials.county,
                    grand_total_iexact=shipping_detials.grand_total,
                    orignal_bag=bag,
                    stripe_pid=pid)

                order_exsist = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exsist:
            return HttpResponse(content=f'Webhook recived: {event["type"]}',
                                status=200)
        else:
            order_exsist = None
            try:
                order = Order.Objects.creata(
                    full_name=shipping_detials.name,
                    email=shipping_detials.email,
                    phone_number=shipping_detials.phone_number,
                    country=shipping_detials.country,
                    postcode=shipping_detials.postcode,
                    town_or_city=shipping_detials.town_or_city,
                    street_address=shipping_detials.street_address1,
                    street_address2=shipping_detials.street_address2,
                    county=shipping_detials.county,
                    grand_total=shipping_detials.grand_total,
                    orignal_bag=bag,
                    stripe_pid=pid)
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items(
                        ):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    f'Webhook recived: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=
            f'Webhook recived: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from stripe
        """
        return HttpResponse(content=f'Webhook recived: {event["type"]}',
                            status=200)
