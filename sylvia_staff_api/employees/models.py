from django.db import models

# Create your models here.
class StaffBase(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_role(self):
        pass
        

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.department} {self.has_company_card} {self.team_size} {self.first_name} {self.last_name} (Manager)"
    
    def get_role(self):
        return "manager"
    
class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='interns')
    internship_end_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Intern)"
    
    def get_role(self):
        return "intern"
    
class Address(models.Model):
    street1_address = models.CharField(max_length=255)
    street2_address = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    
    def str(self):
        return f"{self.street1_address}, {self.street2_address}, {self.house_number}, {self.city}, {self.state}, {self.country}, {self.postal_code}, " 
