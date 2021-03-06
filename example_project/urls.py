from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url=reverse_lazy("music:album_list")), name='home'),
    url(r'^music/', include('music.urls', namespace = 'music')),
)
