from django.conf.urls import url, include
from restaurants import views as res_views

urlpatterns = [
    url(r'^add_restaurant/', res_views.add_restaurant, name="add_restaurant"),
    url(r'^view_restaurants/', res_views.view_restaurants, name="view_restaurants"),
]
