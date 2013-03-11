from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'website.views.home'),
    url(r'^thanks/$', 'website.views.thanks'),
    url(r'^break/$', 'website.views.break_screen'),
    url(r'^csrf/$', 'website.views.csrf'),
    # Examples:
    # url(r'^$', 'psych_app.views.home', name='home'),
    # url(r'^psych_app/', include('psych_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
