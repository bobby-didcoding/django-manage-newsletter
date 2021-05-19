from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from urllib.parse import urlencode
from django.shortcuts import render, redirect
import random


def TokenGenerator():
	
	first = random.randint(1,9)
	first = str(first)
	n = 10

	nrs = [str(random.randrange(10)) for i in range(n-1)]
	for i in range(len(nrs)):
		first += str(nrs[i])

	return str(first)

class NewsLetter(models.Model):

	class Meta:
		verbose_name_plural = "News Letter Subscriptions"
		ordering = ["-timestamp"]

	timestamp = models.DateTimeField()
	updated = models.DateTimeField()

	email = models.EmailField(max_length=254)

	@property
	def is_user(self):
		try:
			user = User.objects.get(email = self.email)
			return True
		except User.DoesNotExist:
			return False

	is_active = models.BooleanField(verbose_name="Subscribed to news letter", default=True)

	token = models.CharField(max_length=100, null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.timestamp = timezone.now()
			self.updated = timezone.now()
			self.token = TokenGenerator()
		super(NewsLetter, self).save(*args, **kwargs)

	reason = models.CharField(verbose_name="Unsubscribe reason", max_length=200, blank=True, null=True)

	def __str__(self):
		return f'{self.email}'

	@property
	def get_params(self):
		params = {
			'email': self.email,
			'token': self.token
		}
		query_string = urlencode(params)
		return "?" + query_string


	def get_absolute_url(self):
		return f"/news-letter"