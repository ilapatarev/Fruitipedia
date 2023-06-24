from django.contrib.auth.hashers import check_password, make_password
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def start_with_letter(value):
	if not value[0].isalpha():
		raise ValidationError('Your name must start with a letter!')
def contains_only_letters(value):
	for ch in value:
		if not ch.isalpha():
			raise ValidationError('Fruit name should contain only letters!')

class Profile(models.Model):
	def set_password(self, raw_password):
		self.password = make_password(raw_password)

	def check_password(self, raw_password):
		return check_password(raw_password, self.password)

	first_name = models.CharField(null=False, blank=False, max_length=25,
	                              validators=[MinLengthValidator(2), start_with_letter], verbose_name='First Name')
	last_name = models.CharField(null=False, blank=False, max_length=35,
	                             validators=[MinLengthValidator(1), start_with_letter], verbose_name='Last Name')
	email = models.EmailField(null=False, blank=False, max_length=40)
	password = models.CharField(null=False, blank=False, max_length=20, validators=[MinLengthValidator(8)])
	image_url = models.URLField(null=True, blank=True, verbose_name='Image URL')
	age = models.IntegerField(null=True, blank=True, default=18)


class Fruit(models.Model):
	name = models.CharField(null=False, blank=False, max_length=30,
	                        validators=[MinLengthValidator(2), contains_only_letters])
	image_url = models.URLField(null=True, blank=True, verbose_name='Image URL')
	description=models.TextField(null=False, blank=False)
	nutrition=models.TextField(null=True, blank=True)
