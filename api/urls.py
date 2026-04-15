from django.urls import include, path

from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('students',views.StudentViewset,basename='students')

urlpatterns = [
    # path('students/',views.studentView),
    # path('students/<int:pk>/',views.studentDetailsView),
    # path('students/',views.StudentsView.as_view()),
    # path('students/<int:pk>/',views.StudentsdetailsView.as_view()),
    path('',include(router.urls)),
]


