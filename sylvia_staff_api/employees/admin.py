from django.contrib import admin
from .models import Manager, Intern, Address

# Register your models here.
admin.site.register(Intern)
admin.site.register(Address)
admin.site.register(Manager)