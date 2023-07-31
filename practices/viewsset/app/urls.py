from django.urls import path
from . import views

urlpatterns = [
    # path('student-api/', views.StudentList.as_view(), name='student-list'),
    # path('student-api/<int:pk>/', views.StudentRetrieve.as_view(), name='student'),
    # path('student-api/create/', views.StudentCreate.as_view(), name='student-create'),
    # path('student-api/<int:pk>/update/', views.StudentUpdate.as_view(), name='student-update'),
    # path('student-api/<int:pk>/delete/', views.StudentDelete.as_view(), name='student-delete'),

    path('student-api/', views.StudentCreateList.as_view(), name='student-api'),
    path('student-api/<int:pk>/', views.StudentUpdateDestroyAPIView.as_view(), name='student-api'),

]