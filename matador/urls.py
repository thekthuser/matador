"""matador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from teams.views import test_member, login_member, index
from django.contrib.auth.views import login, logout

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^test/$', test_member),
    url(r'^test_login/$', login, {'template_name': 'teams/login.html'}, name='login'),
    url(r'^test_index/$', index),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
]
