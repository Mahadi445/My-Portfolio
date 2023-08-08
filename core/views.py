from django.shortcuts import redirect, render
from core.models import Contact,Projects_Data
from core.forms import Data_form
from django.core.paginator import Paginator

from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def Home_page(request):
    return render (request,'core/index.html')
def Resume_page(request):
    return render (request,'core/resume.html') 


#data show using paginator
def Project_page(request):
    projects_list = Projects_Data.objects.all()
    paginator = Paginator(projects_list, 2)  # Show 1 contacts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context={'page_obj': page_obj }
    return render (request,'core/project.html',context)


#admin Data forms
def Project_form_data(request):
    if request.method == 'POST':
        form = Data_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data saved successfully")
            return redirect('Project_Form')
    else:
        form = Data_form()

    return render(request, 'forms/projectForm.html', {'form': form})



#Contact Page Sections Code Here:
def Contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('messages', '')  # Default to an empty string if not provided


        if len(name) == 0  or len(email) == 0 or len(phone) == 0 or  len(description) == 0:
            messages.warning(request, "Please fill in all fields.")
            return redirect ('Contact_page')
        
        else:
            save_data = Contact(name=name,email=email,phone=phone,message=description)
            subject = 'Thanks For Contact'
            message = f'Hi {name}, thank you for your message, We will get back to you soon.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            fail_silently=False,
            send_mail( subject, message, email_from, recipient_list,fail_silently)
            save_data.save()
            messages.success(request, "Thank you successfully sent!")
            return redirect ('Contact_page')    
    else:
        if request.method == "GET":    
            return render (request,'core/contact.html')