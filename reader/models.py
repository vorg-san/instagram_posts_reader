from django.db import models
from django.utils import timezone

class Account(models.Model):
	handle = models.CharField(max_length=400)
	created = models.DateTimeField(default=timezone.now, blank=True)

	def __str__(self):
		return self.handle

class Posts(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	link = models.CharField(max_length=200)
	text = models.CharField(max_length=8000)
	updated = models.DateTimeField(default=timezone.now, blank=True)

	def __str__(self):
		return self.text
