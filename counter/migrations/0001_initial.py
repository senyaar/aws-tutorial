# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(sql="""
BEGIN;
CREATE TABLE "counter_pageview" ("id" serial NOT NULL PRIMARY KEY, "request_time" timestamp with time zone NOT NULL);

COMMIT;
""", state_operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ])]
