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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from website import views as website_views
from teams import urls as teams_urls
from restaurants import urls as res_urls

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', website_views.index, name='index'),
    url(r'^register/$', website_views.register, name='register'),
    url(r'^login/$', login, {'template_name': 'website/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),

    url(r'^team/', include(teams_urls)),
    url(r'^restaurant/', include(res_urls)),

    url(r'^populate/$', website_views.populate, name='populate'),
]
