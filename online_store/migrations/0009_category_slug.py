# Generated by Django 5.0.6 on 2024-07-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0008_alter_products_top_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]