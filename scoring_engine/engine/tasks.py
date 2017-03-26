'''
'''

from celery import shared_task

import models

import importlib
import logging

logger = logging.getLogger(__name__)

@shared_task
def score(service_id):
    '''
    Score a given service with a randomly selected credential.
    '''

    service = models.Service.objects.get(id=service_id)
    credential = service.credentials.order_by('?').first()

    logger.debug('scoring %s for %s with %s using %s' % (
        service, 
        service.team, 
        service.plugin, 
        credential))

    plugin = service.plugin

    m = importlib.import_module('engine.plugins.%s' % plugin.name)
    p = m.Plugin()

    result = models.Result(service=service)

    try:
        success, explanation = p.run(service)

        if success:
            result.status = models.Result.PASSED
            result.explanation = explanation
        else:
            result.status = models.Result.FAILED
            result.explanation = explanation
    except Exception as e: 
        logger.exception(e)
        
        result.status = models.Result.ERROR
        result.explanation = 'Plugin exception'

    result.save()
