from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Contact

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        name_r = request.POST.get('name')
        message_r = request.POST.get('message')


        c = Contact(email=email_r,name=name_r,message=message_r)
        c.save()

        return render(request, 'personal/basic.html')
    else:
        return render(request, 'personal/basic.html')
