# Generated by Django 5.2 on 2025-07-10 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='likes',
        ),
    ]
