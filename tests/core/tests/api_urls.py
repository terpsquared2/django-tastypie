try:
    from django.conf.urls import include, patterns, url
except:  # Django < 1.4
    from django.conf.urls.defaults import include, patterns, url
from core.tests.api import Api, NoteResource, UserResource


api = Api()
api.register(NoteResource())
api.register(UserResource())

urlpatterns = patterns('',
    (r'^api/', include(api.urls)),
)
