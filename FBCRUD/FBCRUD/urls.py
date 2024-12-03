from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.employee_list, name='employee_list'),  # Add name='employee_list'
    path('create/', views.create_employee, name='create'),
    path('update/<int:pk>/', views.update_employee, name='update',), 
    path('delete/<int:pk>/', views.delete_employee, name='delete'),
]
