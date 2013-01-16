from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auth_backend.views.home', name='home'),
    # url(r'^auth_backend/', include('auth_backend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^statinfo/$', 'appname.views.stat_info'),
    #(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'myapp/login.html'}),

    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/accounts/login'}),
    (r'^mainmenu/$', 'appname.views.mainmenu')
)
