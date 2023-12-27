from django.shortcuts import render, redirect , HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
from django.contrib import messages
from .models import *
import re
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request,'index.html')


def admin_reg(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        cpassword =request.POST.get('cpassword')
         # Example: Password should contain at least 8 characters including at least one uppercase letter, one lowercase letter, one digit, and one special character
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        
        if password == cpassword and re.match(password_pattern, password):
            a = regmodel(name=name, email=email, phone=phone, password=password)
            a.save()
            return redirect(admin_log)
        else:
            error_message = "Password requirements: At least 8 characters with one uppercase letter, one lowercase letter, one digit, and one special character."
            return render(request, 'adminreg.html', {'error_message': error_message})
    return render(request,'adminreg.html')

def admin_log(request):
    a = regmodel.objects.all()
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        for i in a:
            if(i.email == email and i.password== password) or  user is not None:
                request.session['a_id']=i.id
                login(request, user) 
                return redirect(admin_index)
        else:
            return HttpResponse("login failed!")
    return render(request,'admin_login.html')

def admin_index(request):
    id1 = request.session['a_id']
    usr = regmodel.objects.get(id=id1)
    name = usr.name
    return render(request,'admin_index.html',{'name':name})

def add_property(request):
    properties = Property.objects.all()
    print(properties)
    if request.method == 'POST':
        if 'property_form' in request.POST:
            form1 = PropertyForm(request.POST)
            if form1.is_valid():
                form1.save()
                messages.success(request, 'Property added successfully!!')
                return redirect('add-property') 

        if 'unit_form' in request.POST:
            
            property_id = request.POST.get('property')
            type = request.POST.get('type')
            rent_cost = request.POST.get('rent_cost')
            image = request.FILES.get('image')
            is_occupied = request.POST.get('is_occupied')
            if is_occupied == 'on':
               is_occupied = True
            else:
               is_occupied = False
            property_instance = Property.objects.get(pk=property_id)
            
            unit_instance = Unit(
                property=property_instance,
                type=type,
                rent_cost=rent_cost,
                image=image,
                is_occupied=is_occupied
            )
            unit_instance.save()
            messages.success(request, 'Unit added successfully!!')
            return redirect('add-property') 
        
        else:
            form1 = PropertyForm(request.POST)
            form2 = UnitForm(request.POST, request.FILES)
            print(form2)
            messages.error(request, 'Form data is invalid.')
    
    return render(request,'add-property.html',{'properties':properties})


def add_assign_tenant(request):
    tenants = Tenant.objects.all()
    units = Unit.objects.all()
    
    if request.method == 'POST':
        if 'tenant_add_form' in request.POST:
            name = request.POST.get('name')
            address = request.POST.get('address')
            file = request.FILES.get('document_proof')
            t = Tenant(name=name,address=address,document_proof=file)
            t.save()
            messages.success(request, 'Tenant details added successfully!!')
            return redirect('add_assign_tenant')

        if 'tenant_assign_form' in request.POST:
            form2 = TenantUnitAssignmentForm(request.POST, request.FILES)
            if form2.is_valid():
                form2.save()
                messages.success(request, 'Tenant Unit Assigned successfully!!')
                return redirect('add_assign_tenant') 

        else:
            form2 = TenantUnitAssignmentForm(request.POST, request.FILES)
            messages.error(request, 'Form data is invalid.')

    else:
        # Initial rendering of the page
        form2 = TenantUnitAssignmentForm()
    return render(request,'add-tenant.html',{'tenants':tenants,'units':units})

def view_property(request):
    tenant_property = TenantUnitAssignment.objects.all()
    pro_name = []
    pro_address = []
    pro_locations = []
    pro_features = []
    
    unit_image = []
    unit_type = []
    unit_rent_cost = []
    unit_is_occu = []
    
    tenant_name = []
    t_add =[]
    t_doc = []
    agg_date = []
    rent_date = []
    
    for i in tenant_property:
        pro_name.append(i.unit.property.name)
        pro_address.append(i.unit.property.address)
        pro_locations.append(i.unit.property.location)
        pro_features.append(i.unit.property.features)
        
        image=str(i.unit.image).split('/')[-1]
        unit_image.append(image)
        
        unit_type.append(i.unit.type)
        unit_rent_cost.append(i.unit.rent_cost)
        unit_is_occu.append(i.unit.is_occupied)
        unit_occ = ['Occupied' if value else 'Not Occupied' for value in unit_is_occu]
        
        tenant_name.append(i.tenant.name)
        t_add.append(i.tenant.address)
        t_doc.append(i.tenant.document_proof)
        agg_date.append(i.agreement_end_date)
        rent_date.append(i.monthly_rent_date)
    mylist=zip(pro_name,pro_address,pro_locations,pro_features,
               unit_image,unit_type,unit_rent_cost,unit_occ
               ,tenant_name,t_add,t_doc,agg_date,rent_date)
    print(pro_name)
    print(pro_address)
    print(rent_date)
    
    return render(request,'property-grid.html',{'tenant_property':mylist})