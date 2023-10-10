from django.db import models

# --------------------------------------------

class Task(models.Model):
	class Status(models.IntegerChoices):
		DRAFT = 0, "Черновик"
		NEW = 1, "Новая"
		PROCESS = 2, "Выполняется"
		DONE = 3, "Выполнена"

	title = models.CharField(max_length=30, verbose_name='Заголовок')
	category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
	description = models.TextField(blank=True, verbose_name='Описание')
	status = models.IntegerField(choices=Status.choices, default=Status.DRAFT, verbose_name='Статус')
	time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
	time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')
	time_deadline = models.DateTimeField(verbose_name='Срок выполнения')
	slug = models.SlugField(unique=True,db_index=True, verbose_name='Slug')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Задача"
		verbose_name_plural = "Задачи"
		ordering = ['-time_create']
		indexes = [
			models.Index(fields=['-time_create'])
		]


class Category(models.Model):
	name = models.CharField(max_length=20, verbose_name='Наименование категории')
	slug = models.SlugField(unique=True,db_index=True, verbose_name='Slug')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"
