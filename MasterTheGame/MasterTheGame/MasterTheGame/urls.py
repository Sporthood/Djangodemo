from django.conf.urls import patterns, include, url

from django.contrib import admin
from api import views
admin.autodiscover()

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^buddy_signup/$', views.buddy_signup, name='buddy_signup'),
url(r'^buddy_login/$', views.buddy_login, name='buddy_login'),
url(r'^forgot_password/$', views.forgot_password, name='forgot_password'),
url(r'^user_login/$', views.user_login, name='user_login'),
]
