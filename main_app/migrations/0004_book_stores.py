# Generated by Django 4.0.3 on 2022-04-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_store_alter_reading_options_alter_reading_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='stores',
            field=models.ManyToManyField(to='main_app.store'),
        ),
    ]
