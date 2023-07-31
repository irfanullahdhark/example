from django.urls import path
from . import views

urlpatterns = [
    # for function based api's

    # path('myapp/',views.hello, name='home'),
    # path('myapp/<int:pk>/',views.hello, name='home2')

    path('myapp/',views.StudentApi.as_view(),name='stuapi'),
    path('myapp/<int:pk>/',views.StudentApi.as_view(),name='stuapi2'),
]