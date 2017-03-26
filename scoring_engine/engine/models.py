'''
'''

from django.db import models


class Plugin(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self.name)


class Team(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self.name)


class Service(models.Model):
    name = models.CharField(max_length=20)
    address = models.GenericIPAddressField()
    port = models.PositiveIntegerField()

    plugin = models.ForeignKey('Plugin', on_delete=models.CASCADE, related_name='services')
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return '%s: %s %s:%d %s' % (
            self.__class__.__name__,
            self.name,
            self.address,
            self.port,
            self.plugin
        )


class Credential(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)

    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='credentials')

    def __str__(self):
        return '%s: %s:%s' % (self.__class__.__name__, self.username, self.password)


class Result(models.Model):
    PASSED = 'passed'
    FAILED = 'failed'
    ERROR = 'error'
    RESULT_CHOICES = (
        (PASSED, 'passed'),
        (FAILED, 'failed'),
        (ERROR, 'error')
    )

    status = models.CharField(max_length=10, choices=RESULT_CHOICES)
    explanation = models.CharField(max_length=25, blank=True)

    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='results')

    def __str__(self):
        return '%s: %s (%s)' % (self.__class__.__name__, self.status, self.explanation)
