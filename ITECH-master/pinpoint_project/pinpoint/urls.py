from django.conf.urls import url
from pinpoint import views


urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^booking/', views.booking, name='booking'),

    url(r'^quiz/', views.quiz, name='quiz'),

    url(r'^destinations/', views.destinations, name='destinations'),

    url(r'^island_page/(?P<destination_name_slug>[\w\-]+)$', views.show_island, name='show_island'),

    url(r'^register/$', views.register, name='register'),

    url(r'^login/$', views.user_login, name='login'),

    url(r'^restricted/', views.restricted, name='restricted'),

    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^restricted/edit/$', views.edit_profile, name='edit_profile'),
    
    url(r'^auth/google/begin/$', views.AuthGoogleBeginView.as_view(), name='auth-google-begin'),
    
    url(r'^auth/google/finished/$', views.AuthGoogleFinishedView.as_view(), name='auth-google-finished'),
    
]
