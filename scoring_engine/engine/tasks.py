'''
'''

from celery import shared_task

import models

import logging

logger = logging.getLogger(__name__)

@shared_task
def score(service_id):
    service = models.Service.objects.get(id=service_id)
    logger.debug('scoring %s for %s with %s' % (service, service.team, service.plugin))
