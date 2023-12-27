from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(regmodel)
admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(TenantUnitAssignment)