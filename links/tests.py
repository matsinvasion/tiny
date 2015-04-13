from django.test import TestCase
from .models import Link
from django.core.urlresolvers import reverse
import random,string

# Create your tests here.

class shortenText(TestCase):
	def test_shorten(self):
		"Test that urls are shortened"
		#a long url for our tests
		url = "http://www.example.com"
		#create url object
		link = Link(url=url)
		#desired short url
		short_url = Link.shorten(link)
		#verify that short_url is always shorter
		self.assertLess(len(short_url),len(url))
	
	def test_link_recovery(self):
		"Test that shortened link and then expanded is the same as original"
		url = "http://www.example.com"
		link = Link(url=url)
		short_url = Link.shorten(link)
		#expanded url
		exp_url = Link.expand_link(short_url)
		self.assertEqual(exp_url,url)
		
	def test_homepage(self):
		"Test that a home page exists and t contains a form"
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)
		self.assertIn("form", response.context)
		
	def test_url_form(self):		
		"Test that submitting form returns a Link objec"
		
		url = "http://www.example.com/"
		response = self.client.post(reverse("home"), {"url":url}, follow=True)
		self.assertEqual(response.status_code,200)
		self.assertIn("link", response.context)
		link = response.context["link"]
		self.assertEqual(url,link.url)
		self.assertIn("link", response.context)
		
	def test_recover_link_n_times(self):
		"Tests multiple times that after shortening and expanding original url is recovered"
		TIMES = 100
		for i in xrange(TIMES):
			uri = "".join(random.sample(string.ascii_letters, 5))
			url = "http://www.example.com/{}/{}".format(i,uri)
			link = Link.objects.create(url=url)
			short_url = Link.shorten(link)
			long_url = Link.expand_link(short_url)
			self.assertEqual(url,long_url)
		
