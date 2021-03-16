from django.urls import path

from . import views

urlpatterns = [
    path("<slug:category>/<slug:slug>/", views.PostDetailView.as_view(), name="detail_post"),
    path("category_<slug:slug>/", views.CategoryView.as_view(), name="category"),
    path("<slug:slug>/", views.TagView.as_view(), name="tags"),


    path('', views.HomeView.as_view()),
]