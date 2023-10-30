from django.urls import path
from myapp.views import ProjectCardList

urlpatterns = [
    path('projectcards/', ProjectCardList.as_view(), name='projectcard-api'),
]
