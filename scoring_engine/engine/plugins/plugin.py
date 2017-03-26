'''
'''

import abc


class Plugin(object):
    '''
    A plugin baseclass to enforce a common interface.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run(self, service, credential=None):
        '''
        Score the service with the given credential. Note: credential may be
        None if no credentials are configured for the given service. Plugins
        requiring credentials which are passed None should raise an error.
        '''

        pass
