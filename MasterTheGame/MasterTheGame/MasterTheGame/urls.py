from django.conf.urls import patterns, include, url

from django.contrib import admin
from api import views
admin.autodiscover()

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^signup/$', views.signup, name='signup'),
]
