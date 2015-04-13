from django.db import models
from basechanger import base_n2decimal, decimal2base_n
from django.core.urlresolvers import reverse

# Create your models here.

class Link(models.Model):
	url = models.URLField()
	
	def get_absolute_url(self):
		return reverse("show_link",kwargs={"pk":self.pk})
	
	@staticmethod
	def shorten(link):
		link,_ = Link.objects.get_or_create(url=link.url)
		return str(decimal2base_n(link.pk))
	
	@staticmethod
	def expand_link(slug):
		link_id = int(base_n2decimal(slug))
		expanded_link = Link.objects.get(pk=link_id)
		return expanded_link.url
	
