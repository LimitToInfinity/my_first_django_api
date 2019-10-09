from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('here_we_go', views.HereWeGoView)

urlpatterns = [
    path("", include(router.urls))
]