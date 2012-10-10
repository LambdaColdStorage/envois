#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
from company import Company
from account import Account
from address import Address
from jinja import Template, Context, FileSystemLoader

class Invoice(object):
    def __init__(self, buyer, seller, items, terms):
        assert(isinstance(buyer, Company))
        assert(isinstance(seller, Company))
        assert(not(isinstance(items, basestring)))
        assert(isinstance(terms, Terms))
        self.buyer = buyer
        self.seller = seller
        self.items = items
        self.terms = terms

    def __repr__(self):
        return "<Invoice: %s, %s>" % (repr(buyer), repr(seller))

    def html(self): 
        """
        self -> HTML
        """
        t = Template('invoice', FileSystemLoader('templates'))
        c = Context(self.context())
        html = t.render(c)
        print(html)

    def context(self):
        """
        self -> { variables to be included in template }
        """
        return merge_dict(self.buyer.context(), self.seller.context(), self.items.context(), self.terms.context())

def merge_dict(*dicts):
    return dict(reduce(lambda a,b: a+b, dicts.items()))

def make_invoice(json_object):
    buyer = Company(**json_object['buyer'])
    seller = Company(**json_object['seller'])
    seller = json_object['items']
    seller = json_object['terms']
    invoice = Invoice(buyer, seller, items, terms)
    return invoice.html()

def main(inp):
    json_object = json.loads(inp.read())
    print(make_invoice(json_object))
    return json_object

if __name__ == "__main__": 
    main(sys.stdin)
