from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^db/', views.count_db, name='db_view'),
    url(r'^cache/', views.count_cache, name='cache_view'),
    url(r'^dynamo/', views.count_dynamo, name='nosql_view'),
    url(r'^$', views.home, name='home_view'),
]
