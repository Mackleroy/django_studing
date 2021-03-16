from django.urls import path

from . import views

urlpatterns = [
    path("tag/<slug:slug>/", views.PostListView.as_view(), name="tags"),
    path("<slug:category_slug>/", views.PostListView.as_view(), name="category"),
    path("<slug:category>/<slug:slug>/", views.PostDetailView.as_view(), name="detail_post"),
    path('', views.PostListView.as_view()),
]