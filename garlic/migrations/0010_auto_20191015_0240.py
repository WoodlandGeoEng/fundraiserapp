# Generated by Django 2.2.5 on 2019-10-15 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garlic', '0009_auto_20191014_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickupLocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(help_text='Location description', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='supporter',
            field=models.CharField(help_text='Supporter name', max_length=40),
        ),
        migrations.AddField(
            model_name='order',
            name='pickupLocation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='garlic.PickupLocations'),
        ),
    ]
