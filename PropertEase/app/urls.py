from django.urls import path
from .views import *

urlpatterns = [
   path('',index),
   path('admin_page/',admin_index,name='admin-index'),
   path('admin_reg/',admin_reg, name='admin-reg'),
   path('admin_log/',admin_log, name='admin-log'),
   path('add_property/',add_property, name='add-property'),
   path('add_assign_tenant/',add_assign_tenant, name='add_assign_tenant'),
   path('view_property/',view_property, name='view_property')
]