#Q-04 What is Django URLs? make program to create django urls
'''
The urls.py file is a crucial component used for URL routing. It defines the mapping between URLs and views, allowing the application to determine which view should handle a specific URL pattern.
from django.urls import path
from . import views
'''

urlpatterns=[
   path('',views.home,name="home"),
   path('product/',views.product,name="product"),
   path('about/',views.about,name="about"),
]