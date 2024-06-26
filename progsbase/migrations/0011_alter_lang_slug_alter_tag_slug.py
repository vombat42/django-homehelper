# Generated by Django 4.2.5 on 2024-03-28 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progsbase', '0010_lang_slug_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lang',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Slug'),
        ),
    ]
