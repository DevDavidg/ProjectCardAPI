from django.contrib import admin
from django.urls import path
from myapp.views import ProjectCardList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projectcards/', ProjectCardList.as_view(), name='projectcard-list'),
]
