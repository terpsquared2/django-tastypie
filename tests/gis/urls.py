try:
    from django.conf.urls import include, patterns, url
except:  # Django < 1.4
    from django.conf.urls.defaults import include, patterns, url

urlpatterns = patterns('',
    (r'^api/', include('gis.api.urls')),
)
