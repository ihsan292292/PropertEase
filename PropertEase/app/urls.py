from django.urls import path
from .views import *

urlpatterns = [
   path('',index, name='index'),
   path('admin_page/',admin_index,name='admin-index'),
   path('admin_reg/',admin_reg, name='admin-reg'),
   path('admin_log/',admin_log, name='admin-log'),
   path('admin_logout/',admin_logout, name='admin_logout'),
   path('add_property/',add_property, name='add-property'),
   path('add_assign_tenant/',add_assign_tenant, name='add_assign_tenant'),
   path('view_property/',view_property, name='view_property'),
   path('property_single/<int:id1>',property_single, name='property_single'),
   path('tenants/',tenants,name='tenants'),
   path('tenant_dtl/<int:id>/',tenant_dtl, name='tenant_dtl')
]