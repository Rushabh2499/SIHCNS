# Generated by Django 3.0.4 on 2020-04-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_dscnwlogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dscnmlogs',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('remarks', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'dscnmlogs',
                'managed': False,
            },
        ),
    ]