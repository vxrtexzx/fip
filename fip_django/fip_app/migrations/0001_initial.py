# Generated by Django 5.1.4 on 2024-12-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Psycho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(blank=True, null=True)),
                ('specialization', models.TextField(blank=True, null=True)),
                ('work_location', models.TextField(blank=True, null=True)),
                ('contacts', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('session', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'psycho',
                'managed': False,
            },
        ),
    ]
