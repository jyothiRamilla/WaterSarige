from django.contrib import admin
from django.urls import path
from  . import views



urlpatterns = [
         path('',views.supply,name="supply"),
         path('index',views.supply,name='supply'),
         
         path('add',views.supply,name='supply'),
         path('loginn.html',views.loginn,name='loginn'),
         path('loginn.html/add',views.supply,name='supply'),
         path('loginn',views.loginn,name='loginn'),
         path('signupp.html',views.signupp,name='signupp'),
         path('signupp',views.signupp,name='signupp'),
         path('signupp.html/add',views.supply,name='supply'),
         path('loginn.html\signupp.html',views.signupp,name='signupp'),
         path('signupp.html\loginn.html',views.loginn,name='loginn'),
         path('vendor.html',views.vendor,name='vendor'),
         path('placetheorder.html',views.placetheorder,name='placetheorder'),
         path('about.html',views.about,name='about'),
         path('index.html',views.supply,name='supply'),
         path('contact.html',views.contact,name='contact'),
         path('legal.html',views.legal,name='legal'),
         path('logout.html',views.logout,name='logout'),
          path('thankyou.html',views.thank,name='thankyou'),
          path('location.html',views.location,name='location'),
]
