'''
'''

from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers

import views

router = routers.DefaultRouter()
router.register(r'plugins', views.PluginViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'credentials', views.CredentialViewSet)
router.register(r'results', views.ResultViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
