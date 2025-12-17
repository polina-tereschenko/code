from django.urls import path
from .views import (
    BlogListView, 
    BlogTextView,
    BlogDetailView, 
    BlogCreateView, 
    BlogUpdateView, 
    BlogDeleteView,
    cv_view,
)

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("text/", BlogTextView.as_view(), name="text"),
    path("cv/", cv_view, name="cv"),
    path("", BlogListView.as_view(), name="home"),
]