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
    queryset = models.Plugin.objects.all()
    serializer_class = serializers.PluginSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

    @detail_route(methods=['POST'])
    def score(self, request, pk=None):
        service = self.get_object()

        tasks.score.delay(service.id)

        return Response({
            'status': 'success',
            'response': 'manual service scoring queued'})


class CredentialViewSet(viewsets.ModelViewSet):
    queryset = models.Credential.objects.all()
    serializer_class = serializers.CredentialSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
