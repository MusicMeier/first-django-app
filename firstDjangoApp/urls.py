from django.urls import path, include
from rest_framework import routers
from .views import DogView


router = routers.DefaultRouter()
router.register('dogs', DogView)

urlpatterns = [
  path('', include(router.urls))
]