from django.shortcuts import render, redirect
from .forms import StudentRegistration, FacultyRegistration, ManagementRegistration

from .models import User, Faculty, Management

#! -------------------------------------------------------------------------------- !#

def homepage(request):
    return render(request, 'home/homepage.html')

#! -------------------------------------------------------------------------------- !#

def view_student(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            registration = User(name=name, email=email, password=password)
            registration.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    student = User.objects.all()
    return render(request, 'student/index.html', {'form': form, 'student': student})


def delete_student(request, id):
    if request.method == 'POST':
        student = User.objects.get(pk=id)
        student.delete()
        return redirect('/student')


def update_student(request, id):
    student = User.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentRegistration(request.POST, instance=student)
        if form.is_valid():
            form.save()
        response = redirect('/student')
        return response
    else:
        form = StudentRegistration(instance=student)
    return render(request, 'student/update.html', {'form': form})


#! -------------------------------------------------------------------------------- !#


def view_faculty(request):
    if request.method == 'POST':
        form = FacultyRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            registration = Faculty(name=name, email=email, password=password)
            registration.save()
            form = FacultyRegistration()
    else:
        form = FacultyRegistration()
    faculty = Faculty.objects.all()
    return render(request, 'faculty/index.html', {'form': form, 'faculty': faculty})


def delete_faculty(request, id):
    if request.method == 'POST':
        faculty = Faculty.objects.get(pk=id)
        faculty.delete()
        return redirect('/faculty')


def update_faculty(request, id):
    student = Faculty.objects.get(pk=id)
    if request.method == 'POST':
        form = FacultyRegistration(request.POST, instance=student)
        if form.is_valid():
            form.save()
        response = redirect('/faculty')
        return response
    else:
        form = FacultyRegistration(instance=student)
    return render(request, 'faculty/update.html', {'form': form})

#! -------------------------------------------------------------------------------- !#

def view_management(request):
    if request.method == 'POST':
        form = ManagementRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            registration = Management(name=name, email=email, password=password)
            registration.save()
            form = ManagementRegistration()
    else:
        form = ManagementRegistration()
    management = Management.objects.all()
    return render(request, 'management/index.html', {'form': form, 'management': management})


def delete_management(request, id):
    if request.method == 'POST':
        managment = Management.objects.get(pk=id)
        managment.delete()
        return redirect('/management')


def update_management(request, id):
    student = Management.objects.get(pk=id)
    if request.method == 'POST':
        form = ManagementRegistration(request.POST, instance=student)
        if form.is_valid():
            form.save()
        response = redirect('/management')
        return response
    else:
        form = ManagementRegistration(instance=student)
    return render(request, 'management/update.html', {'form': form})
