from django.shortcuts import render

# Create your views here.

def student_list(request):
    # Sample data - normally this could come from a database query
    students = [
        {'name': 'John Doe', 'course': 'B.Sc Computer Science'},
        {'name':'uma','course':'BCA'},
        {'name':'Alice Brown', 'course': 'B.A English Literature'},
        {'name': 'Jane Smith', 'course': 'B.A Economics'},
        {'name': 'Emily Johnson', 'course': 'B.Com Accounting'}
    ]
        # Context dictionary - keys will become variable names in the template
    context = {'students': students}
    # Render the template and send the data
    return render(request, 'profiles/student_list.html', context)

def student_fee(request):
    # Sample data - normally this could come from a database query
    fees = [
        { 'course':'B.Sc Computer Science', 'fee': 5000},
        {'course':'BCA','fee':4500},
        {'course':'B.A English Literature','fee':4000},
        {'course':'B.A Economics','fee':3500},
        {'course':'B.Com Accounting','fee':3000}
    ]
        # Context dictionary - keys will become variable names in the template
    context = {'fees': fees}
    # Render the template and send the data
    return render(request, 'profiles/student_fee.html', context)