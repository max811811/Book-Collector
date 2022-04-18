# Generated by Django 4.0.3 on 2022-04-15 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rating', models.CharField(choices=[('A', 'Great'), ('B', 'Medium'), ('C', 'Poor')], default='A', max_length=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.book')),
            ],
        ),
    ]
