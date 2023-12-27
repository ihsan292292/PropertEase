from django import forms
from .models import *

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'location', 'features']
        
class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['property', 'type', 'rent_cost', 'image', 'is_occupied']

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'address', 'document_proof']

class TenantUnitAssignmentForm(forms.ModelForm):
    class Meta:
        model = TenantUnitAssignment
        fields = ['tenant', 'unit', 'agreement_end_date', 'monthly_rent_date']