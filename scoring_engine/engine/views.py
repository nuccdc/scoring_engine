'''
'''

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

import models
import serializers
import tasks

import logging

logger = logging.getLogger(__name__)


class PluginViewSet(viewsets.ModelViewSet):
    queryset = models.Plugin.objects
    serializer_class = serializers.PluginSerializer


class ScoredServiceViewSet(viewsets.ModelViewSet):
    queryset = models.ScoredService.objects
    serializer_class = serializers.ScoredServiceSerializer

    @detail_route(methods=['POST'])
    def score(self, request, pk=None):
        scored_service = self.get_object()
        services = scored_service.services.all()

        for service in services:
            tasks.score.delay(service.id)

        return Response({
            'status': 'success',
            'response': 'manual service scoring queued',
            'services': map(lambda s: s.id, services)
        })


class CheckViewSet(viewsets.ModelViewSet):
    queryset = models.Check.objects
    serializer_class = serializers.CheckSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects
    serializer_class = serializers.TeamSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects
    serializer_class = serializers.ServiceSerializer

    @detail_route(methods=['POST'])
    def score(self, request, pk=None):
        service = self.get_object()

        tasks.score.delay(service.id)

        return Response({
            'status': 'success',
            'response': 'manual service scoring queued',
            'services': [service.id]
        })


class CredentialViewSet(viewsets.ModelViewSet):
    queryset = models.Credential.objects
    serializer_class = serializers.CredentialSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = models.Result.objects
    serializer_class = serializers.ResultSerializer
