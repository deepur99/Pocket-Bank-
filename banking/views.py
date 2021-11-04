from django.shortcuts import render
from . models import *
from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

def home(request):
    return render(request,'banking/home.html')

def about(request):
    return render(request,'banking/about.html')

def contacts(request):
    return render(request,'banking/contacts.html')

def faq(request):
    return render(request,'banking/faq.html')

def customers(request):
    customers_instance = Balance.objects.all()
    return render(request,'banking/customers.html',{'stu':customers_instance})

def insert_data(request):
    try:

        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            email_id = request.POST.get('email_id')
            mobile_no = request.POST.get('mobile_no')
            bank_id = request.POST.get('bank_id')
            address = request.POST.get('address')
            balance = request.POST.get('balance')

            balance_query=Balance.objects.filter(email=email)
            if balance_query:
                return HttpResponse("Given email id Already exists")
            else:
                balance_instance = Balance()
                balance_instance.name=name
                balance_instance.email = email
                balance_instance.email_id = email_id
                balance_instance.mobile_no = mobile_no
                balance_instance.address=address
                balance_instance.balance=balance
                balance_instance.bank_id=bank_id

                balance_instance.save()
            return render(request,'banking/home.html')

        else:
            return render(request,'banking/insert_data.html')

    except Exception as ex:
        print(ex)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')


def transactions(request):
    if request.method == "GET":
        after_instance = After.objects.all()

        return render(request,'banking/transactions.html',{'history':after_instance})


def transfer(request):
    if request.method == "GET":
        email_list = Balance.objects.values('email')
        return render(request,'banking/transfer.html',{'email_list':email_list})

    elif request.method == "POST":
        sender_email = request.POST.get('Sender1')
        receiver_email = request.POST.get('Receiver1')
        amount = request.POST.get('amount1')
        sender_amount = Balance.objects.get(email=sender_email).balance
        print(sender_email,receiver_email)
        receiver_amount = Balance.objects.get(email = receiver_email).balance

        if int(sender_amount) >= int(amount) :
            new_sender_amount = int(sender_amount) - int(amount)
            new_receiver_amount = int(receiver_amount) + int(amount)
            sender_instance = Balance.objects.filter(email=sender_email).update(balance=new_sender_amount)
            receiver_instance = Balance.objects.filter(email=receiver_email).update(balance=new_receiver_amount)
            b = After(sender=sender_email,receiver=receiver_email,amt=amount)
            b.save()
            messages.success(request, f' Transaction was done  successfully')
            print(b.__dict__)
            return HttpResponseRedirect('/transactions/')
        else:
            messages.success(request, f' Transaction Failed')
            return HttpResponseRedirect('/transfer/')
