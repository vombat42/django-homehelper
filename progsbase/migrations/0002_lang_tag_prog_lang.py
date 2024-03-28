# Generated by Django 4.2.5 on 2024-03-23 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('progsbase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Язык программирования')),
            ],
            options={
                'verbose_name': 'Язык программирования',
                'verbose_name_plural': 'Языки программирования',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Тэг')),
                ('progs', models.ManyToManyField(blank=True, null=True, related_name='progs_with_tag', to='progsbase.prog', verbose_name='Программы')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='prog',
            name='lang',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='progsbase.lang', verbose_name='Язык программирования'),
            preserve_default=False,
        ),
    ]