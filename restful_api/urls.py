from django.conf.urls import url, include
from rest_framework import routers
from . import views 

router = routers.DefaultRouter()
router.register('portable_objects', views.Portable_Object_View)

urlpatterns = [

	url(r'^', include(router.urls)),
]