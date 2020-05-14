# Generated by Django 3.0.4 on 2020-05-14 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_delete_mcdo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mcdo',
            fields=[
                ('emp', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='login.Employee')),
                ('topic', models.CharField(max_length=50)),
                ('dop', models.DateTimeField(db_column='DOP')),
                ('content', models.TextField()),
                ('doa', models.DateTimeField(blank=True, db_column='DOA', null=True)),
            ],
            options={
                'db_table': 'mcdo',
                'managed': False,
            },
        ),
    ]
