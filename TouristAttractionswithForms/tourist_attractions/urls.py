from django.urls import path

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("details/<statename>", views.details, name="details"),
  path("state/create", views.StateCreate.as_view(), name="state_create"),
  path("state/update/<int:pk>", views.StateUpdate.as_view(), name="state_update"),
  path("state/delete/<int:pk>", views.StateDelete.as_view(), name="state_delete"),
  path("attraction/create", views.AttractionCreate.as_view(), name="attraction_create"),
  path("attraction/update/<int:pk>", views.AttractionUpdate.as_view(), name="attraction_update"),
  path("attraction/delete/<int:pk>", views.AttractionDelete.as_view(), name="attraction_delete"),
]