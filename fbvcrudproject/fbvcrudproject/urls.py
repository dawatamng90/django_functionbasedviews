from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.retrieve_view, name='home'),
    path('insert/', views.insert_view, name='insert'),
    path('delete/<int:id>/', views.delete_view, name='delete'),
    path('update/<int:id>/', views.update_view, name='update'),
]
