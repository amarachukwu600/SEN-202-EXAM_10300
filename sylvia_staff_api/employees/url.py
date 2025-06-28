from django.urls import path
from .views import StaffRoleView

urlpatterns = [
    path('roles/', StaffRoleView.as_view(), name='staff-roles')
]
