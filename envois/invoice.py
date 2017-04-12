#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
from contextable import Contextable
from terms import Terms
from item import ItemCollection
from company import Company
from constants import DocumentTypes
import jinja2
from hashlib import sha1
import datetime
import subprocess
import os

path = '/'.join(os.path.abspath(__file__).split('/')[:-2])
tenv = (jinja2.Environment(loader=jinja2.FileSystemLoader([
        path + '/templates'])))


def generate_id(n1, n2, LIMIT=5):
    return (sha1('$'.join([n1, n2, str(datetime.datetime.utcnow())]))
            .hexdigest().upper()[:LIMIT])


class Invoice(Contextable):
    def __init__(self, buyer, seller, items, terms, dtype, **kwargs):
        assert(isinstance(buyer, Company))
        assert(isinstance(seller, Company))
        assert(isinstance(terms, Terms))
        self.buyer = buyer
        self.seller = seller
        self.items = items
        self.terms = terms
        self.dtype = dtype
        self.invoice_id = generate_id(self.buyer.name, self.seller.name)
        self.date_of_purchase = kwargs.get('date_of_purchase', '')
        self.purchase_order_no = kwargs.get('purchase_order_no', '')
        self.job_no = kwargs.get('job_no', '')

    def __repr__(self):
        return "<Invoice: {}, {}>".format(repr(self.buyer), repr(self.seller))

    def html(self, dtype=DocumentTypes.INVOICE):
        """
        self -> HTML
        """
        temp = tenv.get_template(self.template(dtype=dtype))
        html = temp.render(self.context())
        return html

    def template(self, dtype, ext='.html'):
        return {dt: dt for dt in DocumentTypes.valid_types()}[dtype] + ext

    def latex(self):
        """
        self -> LaTeX
        """
        temp = tenv.get_template('invoice.tex')
        tex = temp.render(self.context())
        return tex

    def context(self):
        """
        self -> { variables to be included in template }
        """
        # Note the __add__ method on Contextable.
        c = dict(self.buyer.kvl() + self.seller.kvl() + self.items.kvl()
                 + self.terms.kvl())
        c['invoice_id'] = self.invoice_id
        c['title'] = self.seller.name
        c['title_html'] = ('{}-{}_{}'.format(self.seller.name.split(' ')[0],
                                             self.buyer.name.split(' ')[0],
                                             self.dtype)
                                     .lower())
        c['date_of_purchase'] = self.date_of_purchase
        c['purchase_order_no'] = self.purchase_order_no
        c['job_no'] = self.job_no
        return c


def make_invoice(json_object, latex=False,
                 dtype=DocumentTypes.INVOICE):
    buyer, seller = [Company(party, **json_object.pop(party))
                     for party in ['buyer', 'seller']]
    terms = Terms(**json_object.pop('terms'))
    items = ItemCollection(json_object.pop('items'))
    invoice = Invoice(buyer, seller, items, terms, dtype=dtype, **json_object)

    if latex:
        return invoice.latex()
    else:
        return invoice.html(dtype=dtype)


def main(inp, latex, outp, dtype=DocumentTypes.INVOICE):
    json_object = json.loads(inp.read())
    assert(DocumentTypes.validate(dtype))

    if not latex and outp is None:
        print(make_invoice(json_object, dtype=dtype))
    else:
        with open(outp, 'w') as output_file:
            # adding latex macro defs to beginnig of .tex file if
            # user selected latex option
            # this is necessary because jinja syntax and latex macro syntax
            # don't play well together

            # TODO for now, to generate latex, we'll need to be in the
            # top-level dir to have the open statment below find def.tex (give
            # template inheritance another chance??) using sys.argv[0]....? are
            # we sure this script will remain in scripts/  ?
            if latex:
                with open('templates/def.tex', 'r') as tex_defs:
                    defs_content = tex_defs.read()
                    output_file.write(defs_content)
            output_file.write(make_invoice(json_object, latex=latex,
                              dtype=dtype))

    # TODO remove all the .aux, .log, etc. files that are generated as a
    # result of running pdflatex.
    if latex:
        # create .pdf from .tex source generated
        try:
            subprocess.call(["pdflatex", outp])
        except OSError:
            print("you may not have pdflatex installed")
        except:
            print("error generating pdf from latex source file \
                  %s" % outp)

if __name__ == "__main__":
    main(sys.stdin)
