#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contextable import Contextable

class Address(Contextable):
    """
    An address in the invoice
    """
    def __init__(self, **kwargs):
        self.street = kwargs.get('street', '')
        self.city = kwargs.get('city', '')
        self.state = kwargs.get('state', '')
        self.zipcode = kwargs.get('zipcode', '')
        self.phone = kwargs.get('phone', '')
        self.email = kwargs.get('email', '')

    def __str__(self):
        """
        HTML representation
        """
        return """<div class="address">
        %s<br/>
        %s, %s %s<br/>
        %s<br/>
        <a href="mailto:%s">%s</a></div>""" % (self.street, self.city, self.state, self.zipcode, self.phone, self.email, self.email)
