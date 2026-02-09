from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('', views.dashboard),
    path('students/', views.students),
    path('teachers/', views.teachers),
    path('admissions/', views.admissions),
    path('tests/', views.tests),
    path('fees/', views.fees),
    path('activities/', views.activities),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('teacher-dashboard/', views.teacher_dashboard),
    path('student-dashboard/', views.student_dashboard),

]

#from Vidyon import views
#path('teacher/dashboard/',views.teacher_dashboard, name='teacher_dashboard'),

