
from django import forms
from .models import Task, Category
from django.core.exceptions import ValidationError

class AddTaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = '__all__'
		labels = {'slug': 'URL'}

	def clean_title(self):
		title = self.cleaned_data['title']
		if len(title) > 20:
			raise ValidationError('Длина заголовка не должна превышать 20 символов')

		return title