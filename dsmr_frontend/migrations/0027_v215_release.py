# Generated by Django 2.2.9 on 2020-01-07 19:21

from django.db import migrations
from django.utils.translation import ugettext_lazy


def migrate_forward(apps, schema_editor):
    # If someone if using the v3-branch, we no longer require this migration. Code was removed in v3.
    pass


def migrate_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]

    dependencies = [
        ('dsmr_frontend', '0026_v2140_release'),
    ]