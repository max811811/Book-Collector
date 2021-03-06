# Generated by Django 4.0.3 on 2022-04-17 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_reading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='reading',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='reading',
            name='date',
            field=models.DateField(verbose_name='Reading date'),
        ),
    ]
