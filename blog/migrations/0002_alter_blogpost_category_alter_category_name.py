# Generated by Django 5.2 on 2025-07-05 01:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='blog.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Tech', 'Tech'), ('Lifestyle', 'Lifestyle'), ('Travel', 'Travel'), ('Food', 'Food'), ('Education', 'Education'), ('Finance', 'Finance'), ('Entertainment', 'Entertainment')], max_length=100, unique=True),
        ),
    ]
