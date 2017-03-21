#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DocumentTypes(object):
    INVOICE = 'invoice'
    QUOTE = 'quote'
    PACKING_SLIP = 'packing_slip'

    @classmethod
    def valid_types(cls):
        return set([cls.INVOICE, cls.QUOTE, cls.PACKING_SLIP])

    @classmethod
    def validate(cls, dtype):
        return dtype in cls.valid_types()
