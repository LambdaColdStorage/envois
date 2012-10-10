#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Company(object):
    """
    A company in the invoice (both buyer and sellers are companies)
    """
    def __init__(self, name, logo=None, address=None, city=None, state=None, zipcode=None, account={}):
        self.name = name
        self.logo = logo
        self.address = address
        if account.get('same_address', False):
            account['address'] = self.address
        self.account = Account(**account)
