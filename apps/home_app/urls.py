from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'cart$', views.cart),
    url(r'cart/add/(?P<item_id>\d+)$', views.cart),
    url(r'product/(?P<product_id>\d+)$', views.product),
    url(r'products$', views.products),
    url(r'text_page$', views.text_page),
    url(r'logout$', views.logout),
]