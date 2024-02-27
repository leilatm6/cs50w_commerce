# Generated by Django 4.2.1 on 2024-02-27 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_rename_name_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='creatoruser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='products',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(default='No description available'),
        ),
        migrations.AddField(
            model_name='products',
            name='initialprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='title',
            field=models.CharField(default='Unnamed Product', max_length=64),
        ),
    ]