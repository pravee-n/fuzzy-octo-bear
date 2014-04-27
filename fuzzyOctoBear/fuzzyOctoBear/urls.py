from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('fuzzyOctoBear.views',
    # Examples:
    url(r'^$', 'home'),
    url('^eventDetails/', 'eventDetails'),
    url('^get_photos/', 'get_photos'),
    # url('^hello$', 'hello'),
    # url(r'^fuzzyOctoBear/', include('fuzzyOctoBear.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
