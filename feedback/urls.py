from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainFormView.as_view(), name='feedback_form')
]