#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring that correlates two tasks."""

import data
print data.CUSTOMERS
CUSTOMERS = {
1: {'name': 'Ekaterin Vorsoisson', 'email': 'evorsoisson@komarr.net'},
2: {'name': 'Cordelia Naismith', 'email': 'cordelia@beta.com'},
3: {'name': 'Ivan Vorpatril', 'email': 'iv398@barrayar.net'},
4: {'name': 'Aral Vorkosigan', 'email': 'viceroy@sergyar.net'},
5: {'name': 'Eli Quinn', 'email': 'admiral@dendarii.com'},
}

ORDERS = {
27: {'customer_id': 1, 'total': 1},
13: {'customer_id': 1, 'total': 287},
36: {'customer_id': 1, 'total': 999},
4: {'customer_id': 5, 'total': 18},
6: {'customer_id': 4, 'total': 243},
8: {'customer_id': 4, 'total': 536},
15: {'customer_id': 2, 'total': 92},
17: {'customer_id': 3, 'total': 148},
19: {'customer_id': 2, 'total': 159},
21: {'customer_id': 2, 'total': 984},
32: {'customer_id': 5, 'total': 381},
34: {'customer_id': 3, 'total': 183},
35: {'customer_id': 2, 'total': 813},
37: {'customer_id': 3, 'total': 27},
38: {'customer_id': 5, 'total': 52},
39: {'customer_id': 4, 'total': 30},
40: {'customer_id': 2, 'total': 730},
41: {'customer_id': 4, 'total': 28},
42: {'customer_id': 4, 'total': 370},
}


def sum_orders(customers, orders):

    
    """This formula finds the sum of customers orders.

    Args:
        customers(dict): A dictionary of customer_id (required)
        orders(dict): A dictionary of orders keyed by order id (required)

    Returns:
        dictionary: A nested dictionary

    Examples:
    """
 
        

    
    
