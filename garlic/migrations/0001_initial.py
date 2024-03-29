# Generated by Django 2.2.5 on 2019-10-15 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Item name.', max_length=20)),
                ('description', models.CharField(help_text='Brief description of item.', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, help_text='Unit price of item', max_digits=5)),
            ],
        ),
    ]
