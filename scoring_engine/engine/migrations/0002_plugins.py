'''
A hand-written migration using RunPython to load existing plugins into the
database by browsing available modules in plugins/
'''

from __future__ import unicode_literals

from django.db import migrations, models

from engine import plugins

import importlib


def forwards(apps, schema_editor):
    Plugin = apps.get_model('engine', 'Plugin')

    for plugin_name in plugins.__all__:
        try:
            m = importlib.import_module('engine.plugins.%s' % plugin_name)
        except:
            continue

        p = Plugin(name=plugin_name)
        p.save()


def reverse(apps, schema_editor):
    Plugin = apps.get_model('engine', 'Plugin')

    Plugin.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial')
    ]

    operations = [
        migrations.RunPython(forwards, reverse)
    ]
