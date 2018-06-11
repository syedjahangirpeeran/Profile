# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-08 11:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top1', models.CharField(max_length=500)),
                ('top2', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Posts'),
        ),
    ]