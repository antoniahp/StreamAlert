# Generated by Django 4.2.9 on 2024-09-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
