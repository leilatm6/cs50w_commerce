# Generated by Django 4.2.1 on 2024-02-27 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]
