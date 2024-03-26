
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)

from django.shortcuts import redirect, render, get_object_or_404


def employee_form(request, id=None):
    if request.method == "GET":
        if id is None:
            form = EmployeeForm()
        else:
            employee = get_object_or_404(Employee, pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id is None:
            form = EmployeeForm(request.POST)
        else:
            employee = get_object_or_404(Employee, pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect('/employee/list')
        else:
            return render(request, "employee_register/employee_form.html", {'form': form})


def employee_update(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/employee/list')  # Rediriger vers une autre page après la mise à jour
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_register/employee_update.html', {'form': form, 'employee': employee})

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')