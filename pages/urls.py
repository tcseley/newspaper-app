from django.urls import path
from .views import (
    HomePageView, 
    AboutPageView,
    SubmissionPageView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name='about'),
    path('submission/', SubmissionPageView.as_view(), name='submission'),
]