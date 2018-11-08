"""ranking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from rank.views import viewRanking
from rank.views import editRanking
from rank.views import viewEdit
from rank.views import editAllRanking
from rank.views import rEdit
from rank.views import addRanker
from rank.views import delete
from rank.views import deleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', viewRanking, name='main'),
    url(r'^edit/$', viewEdit),
    url(r'^edit/(?P<id>[0-9])/$', editRanking, name='edit'),
    url(r'^editall/$', editAllRanking, name='editall'),
    url(r'^redit/(?P<id>[0-9])/$', rEdit, name='redit'),
    url(r'^add/$', addRanker, name='add'),
    url(r'^delete/(?P<id>[0-9])/$', delete, name='deleteid'),
    url(r'^delete/$', deleteView, name='delete')
]
