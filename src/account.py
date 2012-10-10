#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Account(object):
    """
    A bank account in the invoice
    """
    def __init__(self, bank=None, name=None, number=None, swift=None, account=None):
        self.bank = bank
        self.name = name
        self.number = number
        self.swift = swift
        self.account = account
