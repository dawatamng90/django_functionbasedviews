from django.shortcuts import render, redirect, get_object_or_404
from testapp.models import Employee
from testapp.forms import EmployeeForm

# Create your views here.
def insert_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/')
    else:
        form = EmployeeForm()
    return render(request, 'testapp/insert.html', {'form': form})

# Read your views here.
def retrieve_view(request):
    # Fetch all employee records
    emp_list = Employee.objects.all()
    # Render the response
    return render(request, 'testapp/index.html', {'emp_list': emp_list})

# Update your views here.
def update_view(request, id):
    # Fetch the employee record or return a 404 if not found
    employee = get_object_or_404(Employee, id=id)
    
    if request.method == 'POST':
        # Bind the form to the POST data and the employee instance
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        # Pre-fill the form with the employee instance data
        form = EmployeeForm(instance=employee)
    
    return render(request, 'testapp/update.html', {'form': form})

# Delete your views here.
def delete_view(request,id):
    employee = Employee.objects.get(id = id)
    employee.delete()
    return redirect('/')


    