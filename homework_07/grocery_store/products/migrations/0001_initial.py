# Generated by Django 3.2 on 2023-01-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=164, verbose_name='name')),
                ('weight', models.IntegerField(verbose_name='weight')),
                ('price', models.IntegerField(verbose_name='price')),
            ],
        ),
    ]
