#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contextable import Contextable
from address import Address

class Account(Contextable):
    """
    A bank account in the invoice
    """
    def __init__(self, bank='', name='', number='', routing='', swift='', address='', **kwargs):
        self.bank = bank
        self.name = name
        self.number = number
        self.routing = routing
        self.swift = swift
        assert(isinstance(address, Address))
        self.address = address

    def __str__(self):
        """
        HTML repr
        """
        return """<dl class="account purchase-info">
            <dd>NAME:</dd><dt>%s</dt>
            <dd>ACCOUNT NO.:</dd><dt>%s</dt>
            <dd>ROUTING NO.:</dd><dt>%s</dt>
            <dd>SWIFT:</dd><dt>%s</dt>
            <dd>BANK:</dd><dt>%s</dt>
            <dd>ADDRESS:</dd><dt>%s</dt>
         </dl>
        """ % (self.name, self.number, self.routing, self.swift, self.bank, self.address)

    def context(self):
        """
        self -> { variables to be included in template }
        """
        non_object_kvs = [(k, getattr(self, k, '')) for k in ['bank', 'name', 'number', 'swift', 'routing']]
        non_object_kvs['address'] = self.address.context()
        return dict(non_object_kvs)
