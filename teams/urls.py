from django.conf.urls import url, include
from teams import views as teams_views

urlpatterns = [
    url(r'^edit_member/', teams_views.edit_member, name="edit_member"),
]
