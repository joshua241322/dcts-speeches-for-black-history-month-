from django.urls import path
from .views import submit_speech

urlpatterns = [
    path('', submit_speech, name='submit'),
]
