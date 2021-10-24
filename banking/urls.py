from django.urls import path
from . import views

urlpatterns =[
 path('',views.home,name='home'),
 path('about/',views.about,name='about'),
 path('contacts/',views.contacts,name='contacts'),
 path('customers/',views.customers,name='customers'),
 path('insert_data/',views.insert_data,name='insert_data'),
 path('transfer/',views.transfer,name='transfer'),
 path('transactions/',views.transactions,name='transactions')
]
