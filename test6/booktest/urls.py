from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^text/$',views.text),
    url(r'^show/$',views.show),
    url(r'^set/$',views.set),
    url(r'show_test/$',views.show_test)
]