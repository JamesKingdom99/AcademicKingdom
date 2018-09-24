from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def accounts(request):
    return render(request, 'accounts/login.html')
