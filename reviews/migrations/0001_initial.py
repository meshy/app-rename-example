# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default='', max_length=255, blank=True)),
                ('comment', models.TextField(default='', blank=True)),
                ('rating', models.IntegerField(choices=[(1, '1 out of 5'), (2, '2 out of 5'), (3, '3 out of 5'), (4, '4 out of 5'), (5, '5 out of 5')])),
                ('product', models.ForeignKey(to='catalogue.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
