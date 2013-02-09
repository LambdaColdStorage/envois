#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contextable import Contextable
from currency import Currency

def clean_key(k):
    return ' '.join(k.split('_')).upper()

class Item(Contextable):
    """
    An address in the invoice
    """
    attribute_keys = ['description', 'qty', 'unit_price', 'total_price']
    def __init__(self, description, qty, unit_price, currency="USD"):
        self.description = description
        self.qty = qty
        self.unit_price = Currency(unit_price, currency)
        self.total_price = self.unit_price * qty

    def context(self):
        """
        self -> { 'description': ..., 'qty': ..., 'unit_price': ... }
        """
        c = {
            'vals': Item.attribute_keys
        }
        for val in Item.attribute_keys:
            if hasattr(self, val):
                c[val] = str(getattr(self, val, ''))
        return c

class ItemCollection(Contextable):
    def __init__(self, items):
        self.items = [Item(**i) for i in items]
        self.total = sum(i.total_price for i in self.items)

    def __iter__(self):
        for x in self.items:
            yield x

    def context(self):
        """
        self -> { variables to be included in template }
        """
        return {
            "attribute_keys": [clean_key(k) for k in Item.attribute_keys],
            "items": [i.context() for i in self],
            "total": self.total
        }

