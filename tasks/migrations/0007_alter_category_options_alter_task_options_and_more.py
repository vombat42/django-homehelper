# Generated by Django 4.2.5 on 2023-10-11 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_category_name_alter_task_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-time_create'], 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tasks.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'Черновик'), (1, 'Новая'), (2, 'Выполняется'), (3, 'Периодическая'), (9, 'Выполнена')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_deadline',
            field=models.DateTimeField(verbose_name='Срок выполнения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее изменение'),
        ),
    ]