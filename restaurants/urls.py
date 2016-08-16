from django.conf.urls import url, include
from restaurants import views as res_views

urlpatterns = [
    url(r'^add_restaurant/', res_views.add_restaurant, name="add_restaurant"),
    url(r'^view_restaurants/', res_views.view_restaurants, name="view_restaurants"),
    url(r'^view_restaurant/(?P<pk>\d+)', res_views.view_restaurant, name="view_restaurant"),
    url(r'^add_review/(?P<pk>\d+)', res_views.add_review, name="add_review"),
    url(r'^reviews/(?P<pk>\d+)', res_views.view_user_reviews, name="view_user_reviews"),
]
