# Generated by Django 3.0.5 on 2020-05-06 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dicas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.CharField(max_length=50, verbose_name='email')),
                ('fone', models.CharField(max_length=15, verbose_name='fone')),
            ],
        ),
    ]