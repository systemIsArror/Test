from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PublisherManager(models.Manager):
	def get_queryset(self):
		return super(PublisherManager,self).get_queryset().filter(isDelete=False)

	def create(self,pub_name,pub_address,pub_city,pub_province,pub_website):
		pub = Publisher()
		pub.pub_name = pub_name
		pub.pub_address = pub_address
		pub.pub_city = pub_city
		pub.pub_province = pub_province
		pub.pub_website = pub_website
		pub.save()


class Author(models.Model):
	name = models.CharField(max_length=30)

	class Meta:
		db_table = 'author'

class AuthorInfo(models.Model):
	gender = models.BooleanField(default=False)
	email = models.EmailField()
	address = models.CharField(max_length=100)
	author = models.ForeignKey('Author')

	class Meta:
		db_table = 'authorinfo'

class Publisher(models.Model):
	pub_name = models.CharField(max_length=100)
	pub_address = models.CharField(max_length=100)
	pub_city = models.CharField(max_length=50)
	pub_province = models.CharField(max_length=100)
	pub_website = models.URLField()
	pub_price = models.DecimalField(max_digits=5,decimal_places=2,default=10.00)
	isDelete = models.BooleanField(default=False)


	class Meta:
		db_table = 'publisher'

	pub = PublisherManager()

class Book(models.Model):
	name = models.CharField(max_length=100)
	publish_data = models.DateTimeField()
	author = models.ManyToManyField('Author')
	publish = models.ForeignKey('Publisher')

	class Meta:
		db_table = 'book'


