# Generated by Django 2.2.5 on 2019-10-15 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garlic', '0008_auto_20191014_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='item',
            new_name='purchase',
        ),
    ]