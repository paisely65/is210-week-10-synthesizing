#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring that summarizes customer orders."""

import data

def sum_orders(customers, orders):
    """This formula finds the sum of customers orders.

    Args:
        customers(dict): A dictionary of keyed by customer_id.
        orders(dict): A dictionary of orders keyed by order id
   Returns:
        dictionary: A dictionary that combines customers and orders
   Examples:
        >>>CUSTOMERS = {2: {'name': 'Cordelia Naismith', 'email':
        'cordelia@beta.com'}, 3: {'name': 'Ivan Vorpatril', 'email':
        'iv398@barrayar.net'}},
       >>> ORDERS = {1: {'customer_id': 1, 'total': 10},
             3: {'customer_id': 2, 'total': 10},
             4: {'customer_id': 3, 'total': 15}}
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {3: {'name': 'Ivan Vorpatril',
        'email': 'iv39@barrayar.net'
        'orders': 1,
        'total': 15}
        {2: {'name': 'Cordelia Naismith'
        'email': 'cordelia@beta.com,
        'orders': 2,
        'total': 20}}
    """
    customer_database = {}
    for key, value in customers.iteritems():
        total_orders = 0
        num_orders = 0
        for request in orders.values():
            if key == request['customer_id']:
                total_orders += request['total']
                num_orders += 1
                customer_database[key] = {'name': value['name'],
                                     'email': value['email'],
                                     'orders': num_orders,
                                     'total': total_orders}
    return customer_database
