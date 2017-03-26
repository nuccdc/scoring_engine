'''
'''

import plugin
import os


class Plugin(plugin.Plugin):
    '''
    A ping plugin, simply tests if a host is up py pinging it directly.
    '''

    def run(self, service, credential=None):
        address = service.address

        res = os.system('ping -c 1 {} > /dev/null'.format(address))
        if res == 0:
            return True, ''
        else:
            return False, ''
