from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from .models import Link

# Create your views here.

class CreateLink(CreateView):
	model = Link
	field = ["url"]
	
	def form_valid(self,form):
		prev = Link.objects.filter(url=form.instance.url)
		if prev:
			return redirect("show_link",pk=prev[0].pk)
		return super(CreateLink,self).form_valid(form)
	
class ShowLink(DetailView):
	model = Link
	
class RedirectToLongURL(RedirectView):
	permanet = False
	
	def get_redirect_url(self, *args,**kwargs):
		short_url = kwargs["short_url"]
		return Link.expand_link(short_url)
