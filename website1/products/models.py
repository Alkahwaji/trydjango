from django.db import models


# Create your models here.
class Product(models.Model):
	title       = models.CharField(max_length=120) #max_lenght equals to max length of the title
	description = models.TextField(blank=True, null=True)
	price       = models.DecimalField(decimal_places = 2, max_digits = 10)
	summary     = models.TextField(default='This is cool!')
	
	#To return the title of the field in the admin page	
	def __str__(self):
		return self.title