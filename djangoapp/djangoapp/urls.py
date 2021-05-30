"""djangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teq import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.studentlist.as_view()),
    path('students/add', views.addstudent.as_view()),
    path('students/<int:StudentId>', views.studentdetail.as_view()),
    path('students/edit/<int:StudentId>', views.editstudent.as_view()),
    path('students/delete/<int:StudentId>',views.deletestudent.as_view()),
    path('courses/', views.courselist.as_view()),
    path('courses/add', views.addcourse.as_view()),
    path('courses/<int:CourseId>', views.coursedetail.as_view()),
    path('courses/edit/<int:CourseId>', views.editcourse.as_view()),
    path('courses/delete/<int:CourseId>',views.deletecourse.as_view()),
]
