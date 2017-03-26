'''
'''

from rest_framework import serializers

import models


class PluginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Plugin
        fields = ('id', 'name', )


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Team
        fields = ('id', 'name', 'services')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Service
        fields = ('id', 'name', 'address', 'port', 'plugin', 'team', 'credentials', 'results')
        read_only_fields = ('results', )


class CredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Credential
        fields = ('id', 'username', 'password', 'service')


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Result
        fields = ('id', 'status', 'service', 'explanation')
