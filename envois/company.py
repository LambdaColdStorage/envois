#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contextable import Contextable
from address import Address
from account import Account

class Company(Contextable):
    """
    A company in the invoice (both buyer and sellers are companies)
    """
    def __init__(self, role, name, logo='', address=None, account=None):
        # Don't use mutable objects as default parameters in python.
        address = address if address is not None else {}
        account = account if account is not None else {}

        self.role = role # seller or buyer
        self.name = name
        self.logo = logo
        self.address = Address(**address)
        if account.get('same_address', False):
            account['address'] = self.address
        else:
            account['address'] = Address(**account.get('address', {}))
        self.account = Account(**account)

    def context(self):
        """
        self -> { variaibles to be included in template }
        """
        return {
            self.role: {
                'name': self.name,
                'logo': self.logo,
                'address': self.address,
                'account': self.account
            }
        }
