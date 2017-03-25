'''
'''

from rest_framework import serializers

import models


class PluginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Plugin
        fields = ('name', )


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Team
        fields = ('name', 'services', 'results')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Service
        fields = ('name', 'address', 'port', 'plugin', 'team')


class CredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Credential
        fields = ('username', 'password', 'service')


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Result
        fields = ('status', 'team', 'service')
