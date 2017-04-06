'''
Scoring engine celery tasks.
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
    scored_service = service.scored_service
    credential = service.credentials.order_by('?').first()
    check = service.scored_service.checks.order_by('?').first()

    logger.debug('scoring %s for %s with %s using %s and %s' % (
        service,
        service.team,
        scored_service.plugin,
        credential,
        check))

    plugin = scored_service.plugin

    m = importlib.import_module('engine.plugins.%s' % plugin.name)
    p = m.Plugin()

    result = models.Result(service=service)

    try:
        success, explanation = p.run(service, credential, check)

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
