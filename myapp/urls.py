from django.urls import path
from .views import ProjectCardAPI

urlpatterns = [
    path('projectcards/', ProjectCardAPI.as_view(), name='projectcard-api'),
]
