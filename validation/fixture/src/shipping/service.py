"""Fictional input repository: one sales order can have multiple shipments."""


def shipment_request(sales_order_id, volume):
    return {'sales_order_id': sales_order_id, 'volume': volume, 'status': 'pending'}
