#-----(myapp leval ki urls haii   or project me jo ham url dete haii vo haii------------)



"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('cheader', views.cheader, name='cheader'),
    path('customer_dashboard', views.customer_dashboard, name='customer_dashboard'),
    path('customer_view_policy', views.customer_view_policy, name='customer_view_policy'),
    path('applay/<int:id>', views.applay, name='applay'),
    path('customer_applay_policy', views.customer_applay_policy, name='customer_applay_policy'),
    path('ask_quetion', views.ask_quetion, name='ask_quetion'),
    path('question_history', views.question_history, name='question_history'),
    




    #==========admin=================
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_category', views.admin_category, name='admin_category'),
    path('policy', views.policy, name='policy'),
    path('questions', views.questions, name='questions'),
    path('total_register_user', views.total_register_user, name='total_register_user'),
    path('ac_update/<int:id>', views.ac_update, name='ac_update'),
    path('ac_delete/<int:id>', views.ac_delete, name='ac_delete'),
    path('admin_view_category',views.admin_view_category,name='admin_view_category'),
    path('admin_add_category',views.admin_add_category,name='admin_add_category'),
    path('admin_update_category>',views.admin_update_category,name='admin_update_category'),
    path('edit_category_category/<int:id>',views.edit_category_category,name='edit_category_category'),
    path('admin_delete_category',views.admin_delete_category,name='admin_delete_category'),
    path('delete_category/<int:id>/', views.delete_category, name='delete_category'),

    path('admin_add_policy',views.admin_add_policy,name='admin_add_policy'),
    path('admin_view_policy',views.admin_view_policy,name='admin_view_policy'),
    path('admin_update_policy',views.admin_update_policy,name='admin_update_policy'),
    path('admin_edit_policy/<int:id>',views.admin_edit_policy,name='admin_edit_policy'),
    path('admin_delete_policy',views.admin_delete_policy,name='admin_delete_policy'),
    path('delete_policy/<int:id>',views.delete_policy,name='delete_policy'),
    path('display_questions',views.display_questions,name='display_questions'),
    path('admin_replay_comment/<int:id>',views.admin_replay_comment,name='admin_replay_comment'),
    path('total_applay_policy',views.total_applay_policy,name='total_applay_policy'),
    path('approve/<int:id>/', views.approve_policy, name='approve_policy'),
    path('reject/<int:id>/', views.reject_policy, name='reject_policy'),
    path('rejected',views.rejected,name='rejected'),
    path('approved',views.approved,name='approved'),
    path('wating_approval',views.wating_approval,name='wating_approval'),







]

    

