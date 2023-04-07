from django.urls import path
from .views import ProfileDetail, TesteProfile, UpdateProfilesViews

urlpatterns = [
    path("detail/", ProfileDetail.as_view(), name="detail"),
    path("update/", UpdateProfilesViews.as_view(), name="update_profile")


]