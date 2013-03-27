from django.conf.urls import patterns, url, include
from django. contrib import admin

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', 'website.views.home'),
    url(r'^trial/$', 'website.views.home'),
    url(r'^thanks/$', 'website.views.thanks'),
    url(r'^break/$', 'website.views.break_screen'),
    url(r'^disclaimer/$', 'website.views.disclaimer'),
    url(r'^csrf/$', 'website.views.csrf'),
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
