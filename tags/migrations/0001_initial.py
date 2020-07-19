# Generated by Django 3.0.8 on 2020-07-19 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short', models.CharField(max_length=5)),
                ('color', models.CharField(max_length=7)),
            ],
        ),
    ]