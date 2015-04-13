from django.conf.urls import patterns, include, url
from django.contrib import admin
from links.views import CreateLink, ShowLink, RedirectToLongURL

urlpatterns = patterns('',
    # Examples:
	url(r'^$', CreateLink.as_view(),name="home"),
	url(r'^link/(?P<pk>\d+)$', ShowLink.as_view(), name='show_link'),
	url(r'^r/(?P<short_url>\w+)$', RedirectToLongURL.as_view(),
              name='redirect_short_url'),
    # url(r'^$', 'tiny.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
