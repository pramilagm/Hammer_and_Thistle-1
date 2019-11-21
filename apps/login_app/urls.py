from django.conf.urls import url
from . import views

# Remeber that these follow the extension /login/
urlpatterns = [
    url(r'$', views.login_splash),
    url(r'register$', views.register),
    url(r'logout$', views.logout),
    url(r'login$', views.login),
]