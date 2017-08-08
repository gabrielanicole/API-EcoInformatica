"""apiEigen URL Configuration

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
from rest_framework import serializers, viewsets, routers
from apiv2 import views
#from rest_framework.schemas import get_schema_view


router = routers.DefaultRouter()
router.register(r'tray', views.tra_pingsViewSet)
router.register(r'tower', views.locationViewSet)
router.register(r'ping', views.pingViewSet)
# router.register(r'pingDetail', views.pingDetailViewSet)

# router.register(r'user', views.userViewSet)
# router.register(r'Detail', views.ExampleDFRDetail)

urlpatterns = [
	url('^pht/(?P<horaInicio>.+)(?P<horaFin>.+)(?P<torre>.+)$', views.pingsHorasTorres.as_view()),
	url('^ph/(?P<horaInicio>.+)(?P<horaFin>.+)$', views.pingsHoras.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
