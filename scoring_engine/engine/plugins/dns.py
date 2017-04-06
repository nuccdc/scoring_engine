'''
'''

from __future__ import absolute_import

from . import plugin

from dns import resolver
from dns.exception import *


class Plugin(plugin.Plugin):
    '''
    A plugin to test DNS resolution. Checks are required for this plugin and
    consist of:

    key: [query_type]:[query]
    value: [expected_resolution]
    '''

    def run(self, service, credential=None, check=None):
        address = service.address
        port = service.port

        query_type = check.key.split(':')[0]
        query = check.key.split(':')[1]
        expected_response = check.value

        res = resolver.Resolver()
        res.nameservers = [address]
        res.lifetime = 2.0
        res.timeout = 2.0
        res.port = port

        try:
            response = res.query(query, query_type)[0].to_text()
        except Timeout:
            return False, 'Timeout'
        except (NXDOMAIN, YXDOMAIN, NoAnswer, NoNameservers) as e:
            return False, 'Server error'

        if response == expected_response:
            return True, ''
        else:
            return False, 'Incorrect response'
