#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
from contextable import Contextable
from terms import Terms
from item import Item, ItemCollection
from company import Company
from account import Account
from address import Address
import jinja2
from hashlib import sha1
import datetime
import os

path = '/'.join(os.path.abspath(__file__).split('/')[:-2])
tenv = jinja2.Environment(loader=jinja2.FileSystemLoader([path + '/templates']))

def generate_id(n1, n2, LIMIT=10):
    return sha1('$'.join([n1, n2, str(datetime.datetime.utcnow())])).hexdigest().upper()[:LIMIT]

class Invoice(Contextable):
    def __init__(self, buyer, seller, items, terms, **kwargs):
        assert(isinstance(buyer, Company))
        assert(isinstance(seller, Company))
        assert(isinstance(terms, Terms))
        self.buyer = buyer
        self.seller = seller
        self.items = items
        self.terms = terms
        self.invoice_id = generate_id(self.buyer.name, self.seller.name)
        self.date_of_purchase = kwargs.get('date_of_purchase', '')
        self.purchase_order_no = kwargs.get('purchase_order_no', '')
        self.job_no = kwargs.get('job_no', '')

    def __repr__(self):
        return "<Invoice: %s, %s>" % (repr(buyer), repr(seller))

    def html(self): 
        """
        self -> HTML
        """
        temp = tenv.get_template('invoice.html')
        html = temp.render(self.context())
        return html

    def context(self):
        """
        self -> { variables to be included in template }
        """
        c = merge_dict(self.buyer.context(), self.seller.context(), self.items.context(), self.terms.context())
        c['invoice_id'] = self.invoice_id
        c['title'] = self.seller.name
        c['date_of_purchase'] = self.date_of_purchase
        c['purchase_order_no'] = self.purchase_order_no
        c['job_no'] = self.job_no
        return c

def merge_dict(*dicts):
    return dict(sum([d.items() for d in dicts], []))

def make_invoice(json_object):    
    buyer, seller = [Company(party, **json_object.pop(party)) \
                         for party in ['buyer', 'seller']]    
    terms = Terms(**json_object.pop('terms'))
    items = ItemCollection(json_object.pop('items'))
    invoice = Invoice(buyer, seller, items, terms, **json_object)
    return invoice.html()

def main(inp):
    json_object = json.loads(inp.read())
    return make_invoice(json_object)

if __name__ == "__main__": 
    main(sys.stdin)
