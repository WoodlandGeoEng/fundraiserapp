# Generated by Django 2.2.5 on 2019-10-15 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garlic', '0002_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
    ]
