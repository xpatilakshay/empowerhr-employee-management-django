from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from django.db.models import Q
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.contrib import messages
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import render_to_string




# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




def index(request):
    return render(request,'index.html')


@login_required
def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'view_all.html',context)

@login_required
def add_emp(request):
    if request.method == "POST":
        emp_id = request.POST['emp_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        dept = request.POST['dept']
        role = request.POST['role']
        location = request.POST['location']

        new_emp = Employee(emp_id=emp_id,first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept=dept,role=role,location=location,hire_date=datetime.now())
        new_emp.save()
        messages.success(request, "Employee Added successfully!")
        return redirect('all_emp')
    elif request.method=="GET":
        return render(request,'add_emp.html')
    else:
        return HttpResponse('Something went wrong!....Try again later')


@login_required
def remove_emp(request,emp_id=None):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            messages.success(request, "Employee Removed successfully!")
            return redirect('remove_emp')
        except:
            messages.error(request, "Something went wrong while removing employee.")
            return redirect('remove_emp')
    return render(request,'remove_emp.html',context)


@login_required
def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        location = request.POST['location']
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__icontains = dept)
        if role:
            emps = emps.filter(role__icontains = role)
        if location:
            emps = emps.filter(location__icontains = location)

        context = {
            'emps':emps
        }
        messages.success(request, "Employee Details filtered successfully!")
        return render(request,'view_all.html',context)
    elif request.method == "GET":
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("Something went wrong!...")
    

@login_required
def update_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'update_emp.html', context)


@login_required
def update_details(request, emp_id):
    try:
        emp = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        messages.error(request, "Employee not found.")
        return redirect('update_emp')


    if request.method == 'POST':
        emp.first_name = request.POST['first_name']
        emp.last_name = request.POST['last_name']
        emp.salary = request.POST['salary']
        emp.bonus = request.POST['bonus']
        emp.phone = request.POST['phone']
        emp.dept = request.POST['dept']
        emp.role = request.POST['role']
        emp.location = request.POST['location']

        emp.save()  
        messages.success(request, "Employee updated successfully!")
        return redirect('update_emp')


    context = {'emp': emp}
    return render(request, 'update_details.html', context)



def send_mail_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        full_message = (
    f"New Contact Message\n"
    f"-------------------------------------------------------------------\n"
    f"Name   : {name}\n"
      f"-------------------------------------------------------------------\n"
    f"Email  : {email}\n"
      f"-------------------------------------------------------------------\n"
    f"Subject : {subject}\n"
      f"-------------------------------------------------------------------\n"
    f"Message:\n{message}\n"
    f"-------------------------------------------------------------------"
)


        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                ['akshay434341@gmail.com'], 
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('index')
        except Exception as e:
             messages.error(request, f"Failed to send message: {e}")
             return redirect('index')



def subscribe_newsletter(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')


        html = render_to_string('newsletter_pricing_pdf.html', {'email': user_email})
        result = BytesIO()
        pdf_status = pisa.CreatePDF(html, dest=result)

        if not pdf_status.err:
            try:
                email = EmailMessage(
                    subject="Thanks for Subscribing – Pricing Details Inside",
                    body="Hi there!\n\nThanks for subscribing to EmpowerHR.\nPlease find attached our basic pricing plan.",
                    from_email=settings.EMAIL_HOST_USER, 
                    to=[user_email],
                )
                email.attach('pricing.pdf', result.getvalue(), 'application/pdf')
                email.send()
                messages.success(request, "Thanks for subscribing😊! We've emailed you our pricing PDF.")
            except Exception as e:
                messages.error(request, f"Failed to send email: {e}")
        else:
            messages.error(request, "Error generating PDF.")
        return redirect('index')