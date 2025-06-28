from rest_framework import serializers
from .models import StaffBase, Manager, Intern


class ManagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields ='__all__' 
        read_only_fields = ('id', 'hire_date', 'created_at', 'updated_at', 'has_company_card')

class InternSerializers(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields ='__all__'  
        read_only_fields = ('mentor')

class SafeBaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffBase
        fields ='__all__'                  