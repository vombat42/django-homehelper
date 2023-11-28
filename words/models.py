from django.db import models
# from django.urls import reverse

# --------------------------------------------

class Chapter(models.Model):
	name = models.CharField(max_length=20, unique=True, verbose_name='Раздел')

	class Meta:
		verbose_name = "Раздел"
		verbose_name_plural = "Разделы"

	def __str__(self):
		return self.name


class Word(models.Model):
	name = models.CharField(max_length=30, unique=True, verbose_name='Слово')
	pic = models.ImageField(upload_to='words/pic/', default=None, verbose_name='Изображение')
	voice = models.FileField(upload_to='words/voice/', default=None, verbose_name='Звучание')
	chapter = models.ForeignKey('Chapter', blank=False, null=True, on_delete = models.SET_NULL, verbose_name='Раздел')
	# word_sets = models.ManyToManyField('WordSet', blank=True, null=True, verbose_name='Набор', related_name='word_sets')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Слово"
		verbose_name_plural = "Слова"
		ordering = ['name']
		# indexes = [models.Index(fields=['-time_create'])]

	# def get_absolute_url(self):
		# return reverse('task_details',kwargs={'task_id': self.id})

	# def get_status(self):
		# return self.Status(self.status).label


class WordSet(models.Model):
	name = models.CharField(max_length=30, unique=True, verbose_name='Набор')
	words = models.ManyToManyField('Word', blank=True, null=True, verbose_name='Слова', related_name='words_in_set')

	class Meta:
		verbose_name = "Набор"
		verbose_name_plural = "Наборы"
		ordering = ['name']

	def __str__(self):
		return self.name