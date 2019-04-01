#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ApiPrint():
    def __init__(self, name):
        self.name = name
        self.parameters = []

    def route(self, rule, **options):
        def decorator(f):
            self.parameters.append((rule, f, options))
            return f

        return decorator

    def register(self, blueprint, url_prefix=None):
        for rule, f, options in self.parameters:
            if url_prefix is None:
                url_prefix = '/' + self.name

            endpoint = self.name + '_' + options.pop("endpoint", f.__name__)
            new_rule = url_prefix + rule
            blueprint.add_url_rule(new_rule, endpoint, f, **options)
