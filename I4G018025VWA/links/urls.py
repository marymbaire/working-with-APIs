from django.urls import path
from . import views
from django.contrib import admin

app_name = "links"
urlpatterns= path("api/links/", include("links.urls"))

urlpatterns = [
    path("create/", views.PostCreateApi.as_view(), name="api_create"),
    path("update/<int:pk>", views.PostUpdateApi.as_view(), name="api_update"),
    path("delete/<int:pk>", views.PostDeleteApi.as_view(), name="api_delete"),
    path("", views.PostListApi.as_view(), name="api_list"),
]