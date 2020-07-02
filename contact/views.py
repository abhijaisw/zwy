from django.shortcuts import render
from .models import Contact

# Create your views here.

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, phone=phone, sub=subject, desc=message)
        contact.save()
        thank = True
        return render(request, "contact/contact.html",{'thank':thank})
    return render(request, "contact/contact.html")

