'''
'''

from rest_framework import serializers

import models


class PluginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Plugin
        fields = ('id', 'name', )


class ScoredServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ScoredService
        fields = ('id', 'name', 'plugin', 'checks', 'services')


class CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Check
        fields = ('id', 'key', 'value', 'scored_service')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Team
        fields = ('id', 'name', 'services')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Service
        fields = ('id', 'scored_service', 'address', 'port', 'team', 'credentials', 'results')
        read_only_fields = ('results', )


class CredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Credential
        fields = ('id', 'username', 'password', 'service')


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Result
        fields = ('id', 'status', 'service', 'explanation')
