'''
'''

from django.db import models


class Plugin(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return '{}'.format(self.name)


class Team(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return '{}, id={}'.format(self.name, self.id)


class Service(models.Model):
    name = models.CharField(max_length=20)
    address = models.GenericIPAddressField()
    port = models.PositiveIntegerField()

    plugin = models.ForeignKey('Plugin', on_delete=models.CASCADE, related_name='services')
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return '{} ip={}, port={}, plugin={}'.format(
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
        return '{}:{}'.format(self.username, self.password)


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

    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='results')

    def __str__(self):
        return '{}'.format('PASSED' if self.status else 'FAILED')
