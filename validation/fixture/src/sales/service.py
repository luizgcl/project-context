"""Fictional input repository; deliberately conflicts with the discovery notes."""


def can_cancel(order):
    return order['status'] in {'paid', 'shipped'}


def shipment_payload(order):
    return {'sales_order_id': order['id'], 'items': order['items']}
