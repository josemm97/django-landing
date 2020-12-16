from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'index.html',{})

def contact(request):
    if request.method == 'POST':
        name_contact = request.POST['name']
        email_contact = request.POST['email']
        subject_contact = request.POST['subject']
        message_contact=request.POST['message']
        content='From: '+ email_contact + ' \n'+'Message: '+ message_contact
        send_mail(
           subject_contact,#  Subject here
           content ,  # Here is the message
           email_contact,    #from@example.
           ['jobfreeweb@gmail.com']# ['to@example.com']
            # fail_silenty=False # [fail_silenty=false]
        )
        context={"name": name_contact}  
        return render(request, 'contact.html', context)
    else:
        return render(request,'contact.html',{})

def about(request):
    return render(request,'about.html',{})

def blog(request):
    return render(request,'blog.html',{})
    
def appointment(request):
    if request.method == 'POST':
        name_contact = request.POST['name']
        phone_contact = request.POST['phone']
        email_contact = request.POST['email']
        address_contact = request.POST['address']
        scheldule_contact=request.POST['scheldule']
        date_contact=request.POST['date']
        message_contact=request.POST['message']

        content='Name: '+ name_contact +' \n'+ 'Phone: '+phone_contact + ' \n'+'From: '+ email_contact + ' \n'+'Message: '+ message_contact
        send_mail(
            'Appointment',#  Subject here
            content ,  # Here is the message
            email_contact,    #from@example.
            ['jobfreeweb@gmail.com']# ['to@example.com']
             # fail_silenty=False # [fail_silenty=false]
        )
        context={
            "name":name_contact,
            "phone":phone_contact,
            "email": email_contact,
            "address":address_contact,
            "time":date_contact,
            "schedule": scheldule_contact,
            "message":message_contact
            }  
        return render(request, 'message.html', context)
    else:
        return render(request,'appointment.html',{})