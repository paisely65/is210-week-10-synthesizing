#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring that summarizes sustomer orders."""


def sum_orders(customers, orders):
    """This formula finds the sum of customers orders.

    Args:
        customers(dict): A dictionary of keyed by customer_id.
        orders(dict): A dictionary of orders keyed by order id

    Returns:
        dictionary: A dictionary that combines customers and orders

    Examples:
        >>>CUSTOMERS = 1: {'name': 'Ekaterin Vorsoisson', 'email': 'evorsoisson@komarr.net'},
        2: {'name': 'Cordelia Naismith', 'email': 'cordelia@beta.com'},
        3: {'name': 'Ivan Vorpatril', 'email': 'iv398@barrayar.net'},

        >>> ORDERS = 13: {'customer_id': 1, 'total': 287},
        15: {'customer_id': 2, 'total': 92},
        17: {'customer_id': 3, 'total': 148},
        19: {'customer_id': 2, 'total': 159},
        21: {'customer_id': 2, 'total': 984},
        27: {'customer_id': 1, 'total': 1},
        34: {'customer_id': 3, 'total': 183},
        35: {'customer_id': 2, 'total': 813},
        36: {'customer_id': 1, 'total': 999},
        37: {'customer_id': 3, 'total': 27},
        40: {'customer_id': 2, 'total': 730},

        >>> sum_orders(customers=CUSTOMERS), orders=ORDERS)
    """

    customer_database = {}
    for key, value in customers.iteritems():
        total_orders = 0
        num_orders = 0
        for request in orders.values():
            if key == request['customer_id']:
                total_orders += request['total']
                num_orders += 1
                customer_database = {'name': value['name'],
                                     'email':value['email'],
                                     'orders': num_orders,
                                     'total':total_orders}
    return customer_database
