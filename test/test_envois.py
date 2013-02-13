#-*- coding: utf-8 -*-

"""
    envois.test
    ~~~~~~~~~~~~
    nosetests for the envois pkg

    :copyright: (c) 2012 by Mek
    :license: BSD, see LICENSE for more details.
"""

import os
import json
import unittest
from envois import invoice

jsn = {"seller": {"name": "Lambda Labs, Inc.", "address": {"street": "857 Clay St. Suite 206", "city": "San Francisco", "state": "CA", "zip": "94108",  "phone": "(555) 555-5555", "email": "some@email.com" }, "account": {"swift": "...", "number": "...", "name": "Lambda Labs Inc.", "same_address": True}}, "buyer": {"name": "Foo Corp", "address": {"street": "88 Foo Road, Foo Place", "city": "Fooville", "state": "BA", "zip": "31337"}, "logo": "http://lambdal.com/images/lambda-labs-logo.png"}, "items": [{"description": "Facial Detection & Landmark Recognition Perpetual License", "qty": 1, "unit_price": 32768}], "terms": {"days": 30, "string": ""}}

class Envois_Test(unittest.TestCase):

    def test_invoice(self):
        invoice.make_invoice(jsn)
