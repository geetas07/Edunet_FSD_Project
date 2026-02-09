from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *

def home(request):
  return render(request, 'home.html')

def students(request):
  return render(request, 'students.html', {'data': Student.objects.all()})

def teachers(request):
  return render(request, 'teachers.html', {'data': Teacher.objects.all()})

def admissions(request):
  return render(request, 'admissions.html', {'data': Admission.objects.all()})

def tests(request):
    return render(request, 'tests.html', {'data': Test.objects.all()})

def fees(request):
  return render(request, 'fees.html', {'data': Fees.objects.all()})

def activities(request):
    return render(request, 'activities.html', {'data': Activity.objects.all()})

def teacher_dashboard(request):
  return render(request,'teacher_dashboard.html')

def student_dashboard(request):
  return render(request,'student_dashboard.html')
#from django.db.models import Sum

#def dashboard(request):
    #total_students = Student.objects.count()
    #total_teachers = Teacher.objects.count()
    #total_activities = Activity.objects.count()
    #total_fees = Fees.objects.aggregate(Sum('total_fees'))['total_fees__sum'] or 0

    #context = {
     #  'teachers': total_teachers,
    #       'fees': total_fees
#    }

 #   return render(request, 'dashboard.html', context)
#from django.db.models import Sum

from django.db.models import Sum

def dashboard(request):
    students = Student.objects.count()
    teachers = Teacher.objects.count()
    admissions = Admission.objects.count()
    tests = Test.objects.count()
    activities = Activity.objects.count()
    fees = Fees.objects.aggregate(Sum('total_fees'))['total_fees__sum'] or 0

    context = {
        'students': students,
        'teachers': teachers,
        'admissions': admissions,
        'tests': tests,
        'activities': activities,
        'fees': fees
        
    }
    return render(request, 'dashboard.html', context)
    


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            role = user.profile.role

            if role == 'Admin':
                return redirect('/')
            elif role == 'Teacher':
                return redirect('/teacher_dashboard/')
            else:
                return redirect('/student_dashboard/')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/login/')



