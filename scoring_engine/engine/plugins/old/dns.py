from .. import config

import logging
logger=logging.getLogger(__name__)
from dns import resolver
from dns.exception import *
from dns.resolver import *
import random

ERROR_STRINGS = {
    'NXDOMAIN': 'NXDOMAIN: %s %s',
    'YXDOMAIN': 'Query name too long %s %s',
    'NoAnswer': 'SRVFAIL: %s %s',
    'NoNameservers': 'SRVFAIL: %s %s',
}

def run(options):
    ip = options['ip']
    port = options['port']

    test = random.choice(config.DNS_QUERIES)

    res = resolver.Resolver()
    res.nameservers = [ip]
    res.lifetime = 2.0
    res.timeout = 2.0
    res.port = port

    try:
        response = res.query(test['query'], test['type'])[0].to_text()
    except Timeout:
        logger.debug('Timeout')
        return False
    except (NXDOMAIN, YXDOMAIN, NoAnswer, NoNameservers) as e:
        error_string = ERROR_STRINGS[e.__class__.__name__]
        logger.debug(error_string % (test['query'], test['type']))
        return False

    if response == test['expected']:
        return True
    else:
        logger.debug('Incorrect Response %s' % response)
        return False
