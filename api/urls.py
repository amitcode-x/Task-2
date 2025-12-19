from django.urls import path
from .views import jobs, candidates, applications

urlpatterns = [
    path("jobs", jobs),
    path("candidates", candidates),
    path("applications", applications),
]