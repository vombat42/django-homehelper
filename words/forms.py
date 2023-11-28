from django import forms
from .models import Word, Chapter, WordSet
from django.core.exceptions import ValidationError

# -------------------------------------------------

# class OLD_SelectSetForm(forms.ModelForm):
# 	class Meta:
# 		model = WordSet
# 		fields = '__all__'
# 		# labels = {'slug': 'URL'}


class SelectSetForm(forms.Form):
	queryset = WordSet.objects.all()
	for q in queryset:
		is_select = forms.BooleanField()
