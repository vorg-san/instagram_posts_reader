from django.db import models

class Account(models.Model):
	handler = models.CharField(max_length=400)
	created = models.DateTimeField()

	def __str__(self):
		return self.handler

class Posts(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	text = models.CharField(max_length=8000)
	updated = models.DateTimeField()

	def __str__(self):
		return self.text
