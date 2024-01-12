from django.urls import path,re_path
from . import views
from django.conf.urls import include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'tools',ToolViewSet,basename='tools')

urlpatterns = [
    re_path('', include(router.urls)),
    
]