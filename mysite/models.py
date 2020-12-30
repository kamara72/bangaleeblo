from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name + ' | ' + self.email


class Contactme(models.Model):
	fullname = models.CharField(max_length=50)
	email = models.EmailField()
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.fullname + ' | ' + self.email