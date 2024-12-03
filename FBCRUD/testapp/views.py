from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

# Create an employee
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm()
    return render(request,'testapp/create.html',{'form':form})

# Read employees 
def employee_list(request):
    emp_list = Employee.objects.all()
    return render(request,'testapp/show.html',{'emp_list':emp_list})

# Update an employee
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee) # Bind form with existing employee instance
        if form.is_valid():
            employee.save() # Save the updated data
            return redirect('/')
    else:
        form = EmployeeForm(instance=employee) # Pre-fill form with employee existing data
    return render(request, 'testapp/update.html', {'form': form})

# Delete an employee
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")
    return render(request,'testapp/delete.html',{'employee':employee})


