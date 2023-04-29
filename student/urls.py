from django.urls import path
from . import views


app_name = 'student'
urlpatterns = [
    path('',  views.StudentView.as_view(), name = 'student'),



    # path('<int:id>/', views.postdetail, name = 'postdetail')
]