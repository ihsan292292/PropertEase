from django.db import models

# Create your models here.


class regmodel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Property(models.Model):
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    features = models.TextField()

    def __str__(self):
        return self.name
    
    
class Unit(models.Model):
    PROPERTY_TYPES = (
        ('1BHK', '1 Bedroom, Hall, Kitchen'),
        ('2BHK', '2 Bedrooms, Hall, Kitchen'),
        ('3BHK', '3 Bedrooms, Hall, Kitchen'),
        ('4BHK', '4 Bedrooms, Hall, Kitchen'),
    )
    
    image = models.ImageField(upload_to='property_img')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')
    type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type} - {self.property.name}"
    
class Tenant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    document_proof = models.FileField(upload_to='tenant_documents')
    
    def __str__(self):
        return self.name
    
class TenantUnitAssignment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.PositiveSmallIntegerField()  # Day of the month for rent payment

    def __str__(self):
        return f"{self.tenant.name} - {self.unit.type} - {self.unit.property.name}"
