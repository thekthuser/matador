from django.conf.urls import url, include
from restaurants import views as res_views

urlpatterns = [
    url(r'^add_restaurant/', res_views.add_restaurant, name="add_restaurant"),
]
