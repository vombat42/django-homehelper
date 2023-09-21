from django.db import models

# --------------------------------------------

class Tasks(models.Model):
	title = models.CharField(max_length=20)
	content = models.TextField(blank=True)
	time_create = models.DateTimeField(auto_now_add=True)
	time_update = models.DateTimeField(auto_now=True)
	is_done = models.BooleanField(default=False)



