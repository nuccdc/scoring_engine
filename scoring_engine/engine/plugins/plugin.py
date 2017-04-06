'''
'''

import abc


class Plugin(object):
    '''
    A plugin baseclass to enforce a common interface.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run(self, service, credential=None, check=None):
        '''
        Score the service with the given credential.
        Note: credential and check may both be None if no credentials or checks
        are configured for the given service. Plugins requiring credentials or
        checks which are passed None should raise an error.
        '''

        pass
