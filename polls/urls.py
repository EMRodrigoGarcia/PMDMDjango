from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'question', views.QuestionViewSet)


urlpatterns = [
	path('', include(router.urls)),
	path('', views.index, name='index')
]
