from django.conf.urls import url
from . import views

app_name = 'playbooks'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<playbook_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/unsynced/$', views.unsynced, name='unsynced'),
    url(r'^hosts/(?P<filter_by>[a-zA_Z]+)/$', views.hosts, name='hosts'),
    url(r'^myplaybooks/$', views.playbooks, name='playbooks'),
    url(r'^create_playbook/$', views.create_playbook, name='create_playbook'),
    # url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    # url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    # url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<playbook_id>[0-9]+)/delete_playbook/$', views.delete_playbook, name='delete_playbook'),
]
