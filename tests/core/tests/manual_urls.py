try:
    from django.conf.urls import include, patterns, url
except:  # Django < 1.4
    from django.conf.urls.defaults import include, patterns, url
from core.tests.resources import NoteResource


note_resource = NoteResource()

urlpatterns = patterns('',
    (r'^', include(note_resource.urls)),
)
