# Generated by Django 3.0.8 on 2020-07-19 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '__first__'),
        ('threads', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('task', models.TextField()),
                ('solution', models.TextField()),
                ('difficulty', models.IntegerField()),
                ('coolness', models.IntegerField()),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threads.Thread')),
                ('tags', models.ManyToManyField(to='tags.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]