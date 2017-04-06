'''
'''

from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers

import views

router = routers.DefaultRouter()
router.register(r'plugin', views.PluginViewSet)
router.register(r'scored_service', views.ScoredServiceViewSet)
router.register(r'check', views.CheckViewSet)
router.register(r'team', views.TeamViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'credential', views.CredentialViewSet)
router.register(r'result', views.ResultViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
