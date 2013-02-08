#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contextable import Contextable

class Terms(Contextable):
    """
    An address in the invoice
    """
    def __init__(self, days, string):
        self.days = days
        self.string = string

    def context(self):
        return {
        'terms': {
            'string': self.string,
            'days': self.days
            }
        }
