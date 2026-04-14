from django.urls import include, path

from api import views

urlpatterns = [
    path('students/',views.studentView),
    path('students/<int:pk>/',views.studentDetailsView),
]


