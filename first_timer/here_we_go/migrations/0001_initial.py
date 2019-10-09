# Generated by Django 2.2.4 on 2019-08-28 03:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HereWeGo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('speed', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999)])),
            ],
        ),
    ]
