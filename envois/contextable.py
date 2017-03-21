#!/usr/bin/env python
# -*- coding: utf-8 -*-


def merge_dict(*dicts):
    return dict(sum([d.items() for d in dicts], []))


class Contextable(object):
    def context(self):
        return {}

    def kvl(self):
        # Used for merging contexts.
        return self.context().items()
