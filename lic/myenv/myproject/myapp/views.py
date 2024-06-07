from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import *



# Index page view
def index(request):
    return render(request, "index.html")

# User login view
def login(request):
    if request.POST:
        try:
            # Attempt to authenticate user
            user = User.objects.get(email=request.POST['email'], password=request.POST['pass'])
            request.session['email'] = user.email
            return redirect('customer_dashboard')
        except:
            # Invalid credentials, render login page with error message
            return render(request, 'login.html', {'msg': 'Email and password wrong!!!'})
    else:
        return render(request, "login.html")

# User logout view
def user_logout(request):
    try:
        # Delete user session and redirect to index
        del request.session['email']
        return redirect('index')
    except:
        return redirect('login')

# User signup view




def signup(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            # Check if email already exists
            user = User.objects.get(email=request.POST['email'])
            return JsonResponse({'success': False, 'message': 'Email already exists'})
        except User.DoesNotExist:
            if request.POST['pass'] == request.POST['cpass']:
                # Create new user
                user = User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    no=request.POST['no'],
                    password=request.POST['cpass'],
                )
                return JsonResponse({'success': True, 'message': 'Signup successful'})
            else:
                return JsonResponse({'success': False, 'message': 'Password and Confirm Password do not match'})
    return render(request, 'signup.html')

# Home page view
def home(request):
    return render(request, "home.html")

# Customer header view
def cheader(request):
    # Get user from session
    user = User.objects.get(request.session['email'])
    return render(request, 'cheader.html', {'user': user})

# Customer dashboard view
def customer_dashboard(request):
    return render(request, 'customer_dashboard.html')

# Customer view available policies view
def customer_view_policy(request):
    if 'email' in request.session:
        # Get user from session
        user = User.objects.get(email=request.session['email'])
        # Get policies not applied by the user
        policies = Policy.objects.exclude(policyrecord__user=user)
        return render(request, 'customer_view_policy.html', {'policies': policies})
    else:
        # Redirect to login if user not logged in
        return redirect('login')

# Apply for a policy view
def applay(request, id):
    if 'email' in request.session:
        user = User.objects.get(email=request.session['email'])
        policy = Policy.objects.get(id=id)
        existing_record = PolicyRecord.objects.filter(user=user, policy=policy).exists()
        if existing_record:
            # If policy already applied, display policy record
            policy_record = PolicyRecord.objects.get(user=user, policy=policy)
            return render(request, 'customer_view_policy.html', {'policy_record': policy_record})
        elif request.method == 'POST':
            # Create new policy record
            PolicyRecord.objects.create(user=user, policy=policy, status='Pending')
            return redirect('customer_dashboard')
        else:
            return render(request, 'customer_view_policy.html', {'policy': policy})
    else: 
        return redirect('login')

# Customer view applied policies view
def customer_applay_policy(request):
    try:
        user = User.objects.get(email=request.session['email'])
        user_policy_records = PolicyRecord.objects.filter(user=user)
        return render(request, 'customer_applay_policy.html', {'user_policy_records': user_policy_records})
    except User.DoesNotExist:
        return render(request, 'customer_dashboard.html', {'message': 'User does not exist'})
    except KeyError:
        # Redirect to login if session email not found
        return redirect('login')

# Ask question view
def ask_quetion(request):
    if request.method == 'POST':
        description = request.POST.get('description', '').strip()
        if description:
            # Create new question
            user = User.objects.get(email=request.session['email'])
            question = Question.objects.create(description=description, user=user)
            return redirect('customer_dashboard')
        else:
            return render(request, 'ask_quetion.html')
    else:
        return render(request, 'ask_quetion.html')

# Question history view
def question_history(request):
    # Retrieve the question history along with admin comments
    question_history = Question.objects.filter(admin_comment__isnull=False)
    # Pass the question history to the template
    context = {
        'question_history': question_history
    }
    # Render the template with the provided context
    return render(request, 'question_history.html', context)

# Admin login view
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('admin_dashboard')  
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid Username and Password'})
    return render(request, 'admin_login.html')

# Admin dashboard view
def admin_dashboard(request):
    users = User.objects.all() 
    user_count = users.count()
    questions = Question.objects.all()
    policy_records = PolicyRecord.objects.all()
    policies = Policy.objects.all()
    policy_count = policies.count()
    question_count = questions.count()
    applied_policy_count = policy_records.count()
    return render(request,'admin_dashboard.html',{'users': users,'user_count': user_count,'policies': policies, 'policy_count': policy_count,'question_count': question_count,'applied_policy_count': applied_policy_count})

# Admin logout view
def admin_logout(request):
    logout(request)  
    return redirect('index')  

# View total registered users
def total_register_user(request):
    users = User.objects.all() 
    user_count = users.count()
    return render(request, "total_register_user.html", {'users': users})

# Admin category view
def admin_category(request):
    category = Category.objects.all()
    category_count = category.count()
    return render(request,'admin_category.html',{'category_count':category_count})

# View policy details
def policy(request):
    return render(request,'policy.html')

# View questions
def questions(request):
    return render(request,'questions.html')

# Admin update account view
def ac_update(request,id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return render(request, 'total_register_user.html', {"error": "USER NOT FOUND"})

    if request.method == 'POST':
        # Update user account details
        user.fname = request.POST['fname']
        user.lname = request.POST['lname']
        user.email = request.POST['email']
        user.no = request.POST['no']
        user.save()
        return redirect('total_register_user')
    else:
        return render(request, 'ac_update.html', {'user': user})

# Admin delete account view
def ac_delete(request,id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return redirect('admin_dashboard')
    except User.DoesNotExist:
        return render(request,'total_register_user.html')

# View admin categories
def admin_view_category(request):
    categories = Category.objects.all()
    return render(request, 'admin_view_category.html', {'categories': categories})

# Admin add category view
def admin_add_category(request):
    try:
        if request.POST:
            add_category = Category.objects.create(
                category_name=request.POST['add'],
            )
            return redirect('admin_view_category')
        else:
            return render(request,'admin_add_category.html')
    except:
        return render(request,"admin_add_category.html")

# Admin update category view
def admin_update_category(request):
    categories = Category.objects.all()
    return render(request, 'admin_update_category.html',{'categories':categories})

# Edit category view
def edit_category_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return render(request, 'admin_update_category.html', {"error": "CATEGORY NOT FOUND"})

    if request.method == 'POST':
        category.category_name = request.POST['edit_category']
        category.save()
        return redirect('admin_view_category')  
    else:
        return render(request, 'edit_category_category.html', {'category': category})

# Admin delete category view
def admin_delete_category(request):
    categories = Category.objects.all()
    return render(request,'admin_delete_category.html',{'categories':categories})

# Delete category view
def delete_category(request, id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
        return redirect('admin_view_category')  
    
    except Category.DoesNotExist:
        return render(request, 'admin_view_category.html')

# Admin add policy view
def admin_add_policy(request):
    if request.method == 'POST':
        categories = Category.objects.all()
        try:    
            category_id = request.POST.get('category_id')  
            category = Category.objects.get(pk=category_id)  
            # Create new policy
            policy = Policy.objects.create(
                category=category,  
                policy_name=request.POST['policy_name'],
                sum_assurance=request.POST['sum_assurance'],
                premium=request.POST['premium'],
                tenure=request.POST['tenure'],
            )
            return render(request, 'admin_view_policy.html', {'categories': categories})
        except Exception as e:
            return render(request, 'admin_add_policy.html', {'categories': categories, 'error_message': str(e)})
    else:
        categories = Category.objects.all()
        return render(request, 'admin_add_policy.html', {'categories': categories})

# Admin view policy view
def admin_view_policy(request):
    policies = Policy.objects.all()
    return render(request, "admin_view_policy.html", {'policies': policies})

# Admin update policy view
def admin_update_policy(request):
    policies = Policy.objects.all()
    return render(request,"admin_update_policy.html",{'policies': policies})

# Admin edit policy view
def admin_edit_policy(request, id):
    try:
        policy = Policy.objects.get(id=id)
        categories = Category.objects.all() 
    except Policy.DoesNotExist:
        return render(request, 'admin_view_policy.html', {"error": "Policy not found"})
    
    if request.method == 'POST':
        category_id = request.POST.get('category_id')  
        category = Category.objects.get(pk=category_id)
        policy.policy_name = request.POST['policy_name']
        policy.sum_assurance = request.POST['sum_assurance']
        policy.premium = request.POST['premium']
        policy.tenure = request.POST['tenure']
        policy.category = category  
        policy.save()  

        return redirect('admin_view_policy')
    
    return render(request, 'admin_edit_policy.html', {'policy': policy, 'categories': categories})

# Admin delete policy view
def admin_delete_policy(request):
    policies = Policy.objects.all()
    return render(request,"admin_delete_policy.html",{'policies': policies})

# Delete policy view
def delete_policy(request, id):
    try:
        policy = Policy.objects.get(id=id)
        policy.delete()
        return redirect('admin_view_policy')
    except Policy.DoesNotExist:
        return redirect('admin_view_policy')

# Display questions view
def display_questions(request):
    questions = Question.objects.select_related('user').all()  
    return render(request, 'display_questions.html', {'questions': questions})

# Admin reply to comment view
def admin_replay_comment(request,id):
    question = Question.objects.get(id=id)
    if request.POST:
        question.admin_comment = request.POST['comment']
        question.save()
        return redirect('display_questions')
    else:
        return render(request,"admin_replay_comment.html",{'question':question})

# Total apply policy view
def total_applay_policy(request):
    policy = PolicyRecord.objects.filter(status='Pending')
    return render(request,'total_applay_policy.html',{'policy':policy})

# Approve policy view
def approve_policy(request, id):
    policy = PolicyRecord.objects.get(id=id)
    policy.status = 'Approved'
    policy.save()
    return redirect('admin_dashboard')

# Reject policy view
def reject_policy(request, id):
    policy = PolicyRecord.objects.get(id=id)
    policy.status = 'Rejected'
    policy.save()
    return redirect('admin_dashboard')

# Rejected policies view
def rejected(request):
    rejected_policies = PolicyRecord.objects.filter(status='Rejected')
    return render(request, 'rejected.html', {'rejected_policies': rejected_policies})

# Approved policies view
def approved(request):
    approved_policies = PolicyRecord.objects.filter(status='Approved')
    return render(request, 'approved.html', {'approved_policies': approved_policies})

# Pending approval policies view
def wating_approval(request):
    policy = PolicyRecord.objects.filter(status='Pending')
    return render(request,"wating_approval.html",{'policy':policy}) 
