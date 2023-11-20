# Generated by Django 4.2.5 on 2023-11-20 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Слово')),
                ('pic', models.ImageField(default=None, upload_to='words/pic/', verbose_name='Изображение')),
                ('voice', models.FileField(default=None, upload_to='words/voice/', verbose_name='Звучание')),
                ('chapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='words.chapter', verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Слово',
                'verbose_name_plural': 'Слова',
                'ordering': ['name'],
            },
        ),
    ]
