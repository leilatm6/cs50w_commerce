# Generated by Django 4.2.1 on 2024-02-27 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_title_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
    ]
