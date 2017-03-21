#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DocumentTypes(object):
    INVOICE = 'invoice'
    QUOTE = 'quote'
    PACKING_SLIP = 'packing_slip'
    PURCHASE_ORDER = 'purchase_order'

    @classmethod
    def valid_types(cls):
        return set([cls.INVOICE, cls.QUOTE, cls.PACKING_SLIP, cls.PURCHASE_ORDER])

    @classmethod
    def validate(cls, dtype):
        return dtype in cls.valid_types()
