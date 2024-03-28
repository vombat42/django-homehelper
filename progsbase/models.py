from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# ---------------------------------------------------------------------


class Prog(models.Model):
	"""Программы"""
	title = models.CharField(max_length=30, verbose_name='Заголовок')
	description = models.TextField(blank=True, verbose_name='Описание')
	text = models.FileField(upload_to='progsbase/text/', blank=True, null=True, default=None, verbose_name='Текст программы')
	author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='progs', null=True, default=None, verbose_name='Автор')
	lang = models.ForeignKey('Lang', on_delete=models.PROTECT, related_name='langs', verbose_name='Язык программирования')
	tags = models.ManyToManyField('Tag', blank=True, null=True, verbose_name='Тэги', related_name='tags_of_prog')
	time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
	time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')
	slug = models.SlugField(unique=True,db_index=True, verbose_name='Slug')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('prog-details',kwargs={'prog_slug': self.slug})

	class Meta:
		verbose_name = "Программа"
		verbose_name_plural = "Программы"
		# ordering = ['-time_create']
		# indexes = [models.Index(fields=['-time_create'])]

	# def get_status(self):
	# 	return self.Status(self.status).label


class ProgImage(models.Model):
	"""Список изображений программы"""
	prog = models.ForeignKey('Prog', related_name='images', on_delete = models.CASCADE, verbose_name='Программа')
	image = models.ImageField(upload_to='progsbase/pic/', verbose_name='Изображение')
	description = models.TextField(blank=True, null=True, verbose_name='Описание')
	
	class Meta:
		verbose_name = "Изображение программы"
		verbose_name_plural = "Изображения программы"


class ProgLink(models.Model):
	"""Список ссылок программы"""
	prog = models.ForeignKey('Prog', related_name='links', on_delete = models.CASCADE, verbose_name='Программа')
	link = models.URLField(verbose_name='Ссылка')
	description = models.TextField(blank=True, null=True, verbose_name='Описание')
	
	class Meta:
		verbose_name = "Ссылка программы"
		verbose_name_plural = "Ссылки программы"


class Lang(models.Model):
	"""Языки программирования"""
	name = models.CharField(max_length=20, unique=True, verbose_name='Язык программирования')
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

	class Meta:
		verbose_name = "Язык программирования"
		verbose_name_plural = "Языки программирования"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('progs-lang', kwargs={'lang_slug': self.slug})


class Tag(models.Model):
	"""Тэги программ"""
	name = models.CharField(max_length=30, unique=True, verbose_name='Тэг')
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

	class Meta:
		verbose_name = "Тэг"
		verbose_name_plural = "Тэги"
		ordering = ['name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('progs-tag', kwargs={'tag_slug': self.slug})