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
url(r'^user_signup/$', views.user_signup, name='user_signup'),
url(r'^get_user_details/$', views.get_user_details, name='get_user_details'),
url(r'^add_state/$', views.add_state, name='add_state'),
url(r'^add_city/$', views.add_city, name='add_city'),
url(r'^add_sport/$', views.add_sport, name='add_sport'),
url(r'^add_location/$', views.add_location, name='add_location'),
url(r'^create_session/$', views.create_session, name='create_session'),
url(r'^join_session/$', views.join_session, name='join_session'),
url(r'^remove_session/$', views.remove_session, name='remove_session'),
url(r'^player_sessions/$', views.player_sessions, name='player_sessions'),
url(r'^player_rating/$', views.player_rating, name='player_rating'),
url(r'^create_rating/$', views.create_rating, name='create_rating'),
url(r'^endurance_graph/$', views.endurance_graph, name='endurance_graph'),
url(r'^weight_graph/$', views.weight_graph, name='weight_graph'),


]
