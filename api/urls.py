from django.urls import include, path

from api import views

urlpatterns = [
    # path('students/',views.studentView),
    # path('students/<int:pk>/',views.studentDetailsView),
    path('students/',views.StudentsView.as_view()),
    path('students/<int:pk>/',views.StudentsdetailsView.as_view()),
]


