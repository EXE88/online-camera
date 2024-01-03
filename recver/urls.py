from django.urls import path
from . import views

urlpatterns = [
    path('',views.CameraDisplay.as_view(),name='camera_display_page')
]
