from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns =[
 path('',views.home,name='home'),
 path('about/',views.about,name='about'),
 path('contacts/',views.contacts,name='contacts'),
 path('customers/',views.customers,name='customers'),
 path('insert_data/',views.insert_data,name='insert_data'),
 path('transfer/',views.transfer,name='transfer'),
 path('transactions/',views.transactions,name='transactions'),
 path('login/',auth_view.LoginView.as_view(template_name='banking/login.html'),name='login'),
 path('logout/',auth_view.LogoutView.as_view(template_name='banking/logout.html'),name='logout'),
 path('register/',views.register,name='register'),
 path('profile/', views.profile, name='profile'),
 path('faq/', views.faq, name='faq'),
]
