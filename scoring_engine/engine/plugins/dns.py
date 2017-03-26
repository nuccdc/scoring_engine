'''
'''

from __future__ import absolute_import

from . import plugin

from dns import resolver
from dns.exception import *

class Plugin(plugin.Plugin):
    '''
    A plugin to test DNS resolution.
    '''
    
    # TODO for now this only checks that google.com resolves. Ideally, we
    # should be able to provide a list of domains and their expected ip
    # addresses to check against. Perhaps this should be a model with a foreign
    # key to team - ie DnsRecord. Or maybe it should be stored in a
    # configuration file, rather than the database.

    def run(self, service, credential=None):
        address = service.address
        port = service.port
        query = 'google.com'
        query_type = 'A'
        expected_response = ''

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

        # TODO once we have a way to store configuration, we should check to
        # see if the response matches what is expected. For now, just return
        # True.
        """
        if response == expected_response:
            return True, ''
        else:
            return False, 'Incorrect response'
        """

        return True, ''
