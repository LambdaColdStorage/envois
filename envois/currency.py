#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contextable import Contextable
from numbers import Number
import locale
try:
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')
except:
    try:
        locale.setlocale(locale.LC_ALL, 'en_US')
    except:
        locale.setlocale(locale.LC_ALL, 'POSIX')

SYMBOL = {
    'USD': "$"
}


class Currency(Contextable):
    """
    An address in the invoice
    """
    supported = ['USD']

    def __init__(self, amt, currency):
        self.amt = amt
        assert(currency.upper() in Currency.supported)
        self.currency = currency.upper()

    def __add__(self, other):
        if isinstance(other, Number) and other == 0:
            return self
        assert(isinstance(other, Currency))
        assert(other.currency == self.currency)
        return Currency(self.amt + other.amt, self.currency)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        assert(isinstance(other, Currency))
        assert(other.currency == self.currency)
        return Currency(self.amt - other.amt, self.currency)

    def __mul__(self, other):
        assert(isinstance(other, Number))
        return Currency(self.amt * other, self.currency)

    def __div__(self, other):
        assert(isinstance(other, Number))
        return Currency(self.amt / other, self.currency)

    def __str__(self):
        return "%s%s %s" % (SYMBOL[self.currency],
                            locale.format("%d", self.amt, grouping=True),
                            self.currency)
