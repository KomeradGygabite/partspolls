import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Part(models.Model):
	name = models.CharField(max_length=200)
	inventory = models.PositiveSmallIntegerField()
	cost = models.DecimalField(max_digits=6, decimal_places=2)
	pub_date = models.DateTimeField('date published')
	update_date = models.DateTimeField('date updated')
	long_desc = models.CharField(max_length=1000)
	short_desc = models.CharField(max_length = 300)

	category_choices = (
		('AI', 'Air Intake'),
		('BK', 'Brakes'),
		('CL', 'Cooling'),
		('DT', 'Drivetrain and Transmission'),
		('EC', 'Electronics'),
		('EG', 'Engine'),
		('EX', 'Exhaust'),
		('FC', 'Fuel Components'),
		('GH', 'Gauges and Gauge Holders'),
		('IG', 'Ignition Components'),
		('IC', 'Intercoolers'),
		('IT', 'Interior'),
		('SL', 'Silicon Couplers and Hoses'),
		('SF', 'Safety'),
		('SP', 'Suspension'),
		('TK', 'Turbochargers and Kits'),
		('WG', 'Wastegates'),
		('MC', 'Miscellanious'),
		('TM', 'Turbocharger accessories and kits'),
	)
	category = models.CharField(
		max_length=2,
		choices=category_choices,
		default='AI',
		)

	def __str__(self):
		return self.name
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	def was_updated_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.update_date <= now
	def in_stock(self):
		if self.inventory == 0:
			return False
		elif self.inventory > 0:
			return True
		else:
			return False #There was an error so resort to false.

	was_published_recently.admin_order_field = 'pub_date'
	was_updated_recently.admin_order_field = 'update_date'
	in_stock.admin_order_field = 'inventory'

	was_published_recently.boolean = True
	was_updated_recently.boolean = True
	in_stock.boolean = True

	was_published_recently.short_description = 'Published Recently'
	was_updated_recently.short_description = 'Updated Recently'
	in_stock.short_description = 'In Stock'
