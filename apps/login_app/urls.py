from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'$', views.login_splash),
    url(r'register$', views.register),
    url(r'logout$', views.logout),
    url(r'login$', views.login),
    url(r'dashboard$', views.dashboard),
]