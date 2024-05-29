from django.shortcuts import render,redirect
from .models import *
# from django.db.models import Q
from django.contrib import messages
from django.conf import settings
import requests
import random
import razorpay
#from .utils import *
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache

# Create your views here.

def home(request):
    return render(request,"Welcome to the homepage !")
@never_cache
def sindex(request):
    product=Product()
    product=Product.objects.all()
    return render(request,"sindex.html",{'product':product})

@never_cache
def index(request):
    # user=User.objects.get(email=request.session['email']) 
    # if user.role == "buyer":
    #     return render(request,"index.html")
    # else:
        product=Product()
        product=Product.objects.all()
        
        return render(request,"index.html",{'product':product})

@never_cache
def about(request):
    return render(request,"about.html")

@never_cache
def blog(request):
    return render(request,"blog.html")

@never_cache
def shop(request,cat):
    product=Product()
    if cat == "all":
        product=Product.objects.all()
    
    elif cat == "women":
        product=Product.objects.filter(pcategory="Women")
    
    elif cat == "men":
        product=Product.objects.filter(pcategory="Men")

    elif cat == "child":
        product=Product.objects.filter(pcategory="Child")

    return render(request,"product.html",{'product':product})

@never_cache
def contact(request):
    return render(request,"contact.html")

@never_cache
def header(request):
    return render(request,"header.html")

@never_cache
def signup(request):    

    if request.method=="POST":

        try:
            User.objects.get(email=request.POST['email'])
            messages.error(request,"Email is Already Registered !!")
            return render(request,"signup.html")
        
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    role=request.POST['role'],
                    email = request.POST['email'],
                    firstname= request.POST['firstname'],
                    lastname= request.POST['lastname'],
                    mobile= request.POST['mobile'],
                    password= request.POST['password']
                )

                messages.success(request,"Registration Successfully..")
                return render(request,"login.html")
            
            else:
                messages.error(request,"Password & Confirm password does not match !!")
                return render(request,"signup.html")
            
    else:
        return render(request,"signup.html")

@never_cache
def login(request):

    if request.method=="POST":

        try:
            
                user=User.objects.get(email=request.POST['email'])
                if user.password==request.POST['password']:
                    if user.role=="buyer":
                        request.session['email']=user.email
                        request.session['firstname']=user.firstname
                        wishlist=Wishlist.objects.filter(user=user)
                        request.session['wishlist']=len(wishlist)
                        cart=Cart.objects.filter(user=user,payment_status=False)
                        request.session['cart']=len(cart)
                        return render(request,'index.html')
                    else:
                        request.session['email']=user.email
                        request.session['firstname']=user.firstname
                        return render(request,'sindex.html')
                
                else:
                    messages.error(request,"Password does not match !!")
                    return render(request,"login.html")


        except:
                messages.error(request,"Email is not registered !!")
                return render(request,"signup.html")

    else:
        return render(request,"login.html") 
    

@never_cache
def logout(request):

    try:
        del request.session['email']
        del request.session['firstname']
        del request.session['wishlist']
        del request.session['cart']
        logout(request)
        request.session.set_expiry(0)
        return redirect(login)
    except:
        return redirect(index)

    

def fpassword(request):

    if request.method=="POST":
        try:
            #   user= User.objects.get(mobile=request.POST['mobile'])
            #   mobile= request.POST['mobile']
              otp= random.randint(1001,9999)

              url = "https://www.fast2sms.com/dev/bulkV2"

              querystring = {"authorization":"kQ809jGzAmRf3CV1vOM2bto6IgB7ayPNxJhETLZcKUreDsFwnipMgqC3IH2Rk1dWscQx5EX689FJzwUK","variables_values":str(otp),"route":"otp","numbers":request.POST['mobile']}

              headers = {
                            'cache-control': "no-cache"
                        }

              response = requests.request("GET", url, headers=headers, params=querystring)
              request.session['mobile']=request.POST['mobile']
              request.session['otp']=otp
              return render(request,"otp.html")
         
        except:
              return render(request,"fpassword.html")  
    else:
         return render(request,"fpassword.html")
    

def otp(request):
    if request.method=="POST":
        otp= int(request.session['otp'])
        otp= int(request.POST['otp'])

        if otp==otp:
            del request.session['otp']
            return render(request,"newpassword.html") 

        else:
            messages.error(request,"Invalid Otp !")     
            return render(request, "newpassword.html") 
        
    else:
        return render(request,"otp.html")
    
def fpassword_email(request):
          
          if request.method=="POST":
            email= request.POST['email']
            request.session['email']=request.POST['email']
            
            passw= random.randint(100001,999999)
            request.session['passw']=passw
            mymailfunction("Welcome to Myapp","mymailtemplate",email,{'email':email,"passw":passw})
            return render(request,"password.html")
          
          else:
            return render(request,"fpassword_email.html")
          
def password(request):
     if request.method=="POST":
        password= int(request.session['passw'])
        upassword= int(request.POST['password'])

        if password==upassword:
            del request.session['passw']
            return render(request,"email_newpassword.html") 

        else:
            messages.error(request,"Invalid Password !")     
            return render(request, "email_newpassword.html") 
        
     else:
        return render(request,"password.html")
     
def email_newpassword(request):
     if request.method=="POST":
               user= User.objects.get(email=request.session['email'])

               if request.POST['e_newpassword']==request.POST['e_cpassword']:
                    user.password=request.POST['e_newpassword']
                    user.save()
                    return render(request,"login.html")
               
               else:
                    messages.error(request,"New Password and Confirm Password does not match !!")
                    return render(request,"email_newpassword.html")
          
     else:
          return render(request,"email_newpassword.html")
    
def newpassword(request):
    if request.method=="POST":         
               user= User.objects.get(mobile=request.session['mobile'])

               if request.POST['newpassword']==request.POST['cpassword']:
                    user.password=request.POST['newpassword']
                    user.save()
                    return render(request,"login.html")
               
               else:
                    messages.error(request,"New Password and Confirm Password does not match !!")
                    return render(request,"newpassword.html")
    else:
          return render("newpassword.html")
    

@never_cache                 
def changepassword(request):
    try:
        user= User.objects.get(email=request.session['email'])

        if request.method=="POST":
            if user.password==request.POST['oldpassword']:
                if request.POST['newpassword']==request.POST['cpassword']:
                    user.password=request.POST['newpassword']
                    user.save()
                    return redirect("logout")
                
                else:
                    messages.error(request,"New Password and Confrim Password doest not match !!")
                    if user.role=="buyer":
                        return render(request,"changepassword.html")
                    else:
                        return render(request,"scpassword.html")

            else:
                messages.error(request,"Old Password does not match !!")
                if user.role=="buyer":
                    return render(request,"changepassword.html")
                else:
                    return render(request,"scpassword.html")
        else:    
            if user.role=="buyer":
                return render(request,"changepassword.html")
            else:
                return render(request,"scpassword.html") 
    
    except:
        return redirect(index)
        

@never_cache
def profile(request):

    try:
        uemail=request.session['email']
        data=User.objects.get(email=uemail)
        messages.success(request,"Profile Updates Successfullyy...")
        if data.role=="buyer":
            return render(request,"profile.html",{'data':data})
        else:
            return render(request,"sprofile.html",{'data':data})
    
    except Exception as e:
        print("error\n",e)
        return redirect(index)

@never_cache
def addproduct(request):
    seller=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        Product.objects.create(
            seller=seller,
            pcategory=request.POST['pcategory'],
            psize=request.POST['psize'],
            pbrand=request.POST['pbrand'],
            price=request.POST['price'],
            desc=request.POST['desc'],
            pname=request.POST['pname'],
            picture=request.FILES['picture']
        )

        messages.success(request,"Product Added Successfully..")
        return render(request,"addproduct.html")
    
    else:
        return render(request,"addproduct.html")

@never_cache
def viewproduct(request,cat):
    try:
        seller=User.objects.get(email=request.session['email'])
        product=Product.objects.filter(seller=seller)

        # product=Product()
        if cat == "all":
            product=Product.objects.all()
        
        elif cat == "women":
            product=Product.objects.filter(pcategory="Women")
        
        elif cat == "men":
            product=Product.objects.filter(pcategory="Men")

        elif cat == "child":
            product=Product.objects.filter(pcategory="Child")

        return render(request,"viewproduct.html",{'product':product})
    except:
        return redirect("index")

def pdetail(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,"pdetail.html",{'product':product})


def edit(request,pk):
    product=Product.objects.get(pk=pk)
    if request.method=="POST":
        product.pcategory=request.POST['pcategory']
        product.psize=request.POST['psize']
        product.pbrand=request.POST['pbrand']
        product.pname=request.POST['pname']
        product.price=request.POST['price']
        product.desc=request.POST['desc']

        try:
            product.picture=request.FILES['picture']
        except:
            pass
        product.save()
        messages.success(request,"Product Updated Successfully...")
        return render(request,"edit.html",{'product':product})

    else:
        return render(request,"edit.html",{'product':product})

def delete(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect(sindex)

@never_cache
def bpdetail(request,pk):
    try:
        w=False
        c=False
        user= User.objects.get(email=request.session['email'])
        product=Product.objects.get(pk=pk)

        try:
            Wishlist.objects.get(user=user, product=product)
            w = True
        
        except:
            pass

        try:
            Cart.objects.get(user=user,product=product,payment_status=False)
            c=True
        
        except:
            pass

        return render(request,"bpdetail.html",{'product':product,'w':w,'c':c})
    except:
        product=Product.objects.get(pk=pk)
        return render(request,"bpdetail.html",{'product':product})


def addwish(request,pk):
    user= User.objects.get(email=request.session['email'])
    product= Product.objects.get(pk=pk)
    # Wishlist.objects.create(user=user,product=product)
    if not Wishlist.objects.filter(user=user, product=product).exists():
        # If not, add the product to the wishlist
        Wishlist.objects.create(user=user, product=product)
    return redirect("wishlist")

@never_cache
def wishlist(request):
    try:
        user= User.objects.get(email=request.session['email'])
        wishlist=Wishlist.objects.filter(user=user)
        request.session['wishlist']=len(wishlist)
        return render(request,"wishlist.html",{'wishlist':wishlist})
    except:
        return redirect(index)

def removewish(request,pk):
    user= User.objects.get(email=request.session['email'])
    product= Product.objects.get(pk=pk)
    wishlist= Wishlist.objects.get(user=user,product=product)
    wishlist.delete()
    return redirect("wishlist")

@never_cache
def scart(request):
    try:
        user=User.objects.get(email=request.session['email'])
        order=Order.objects.filter(user=user).first()
        cart=Cart.objects.filter(user=user,payment_status=False)
        request.session['cart']=len(cart)

        if request.method=="POST":
            Order.objects.create(user=user,
                                address=request.POST['address'],
                                pincode=request.POST['pincode']
                            )
            return render(request,"scart.html",{'cart':cart,'user':user})
           
        else:
            return render(request,"scart.html",{'cart':cart,'user':user,'order':order})
    
    except User.DoesNotExist:
        return redirect("index")


def addcart(request,pk):
    product= Product.objects.get(pk=pk)
    user= User.objects.get(email=request.session['email'])
    Cart.objects.create(user=user,
                        product=product,
                        product_qty=1,
                        product_price=product.price, 
                        total_price=product.price,
                        )
    return redirect("scart")

def removecart(request,pk):
    product=Product.objects.get(pk=pk)  
    user=User.objects.get(email=request.session['email'])
    cart= Cart.objects.get(user=user,product=product,payment_status=False)
    cart.delete()
    return redirect("scart")

def change_qty(request):
    pk=request.POST['id']
    print(pk)
    product_qty=int(request.POST['product_qty'])
    cart=Cart.objects.get(pk=pk)
    cart.product_qty=product_qty
    cart.total_price=cart.product_price*product_qty
    cart.save()

    return redirect('scart')

@never_cache
def checkout_detail(request):
    if request.method=="POST":
        try:
            net_price=0
            user=User.objects.get(email=request.session['email'])
            cart=Cart.objects.filter(user=user,payment_status=False)
            order=Order.objects.filter(user=user).first()
            request.session['cart']=len(cart)

            for i in cart:
                net_price+=i.total_price

                if net_price >= 20000:
                    shipping_charge=0
                else:
                    shipping_charge=100
                
            t=int(net_price+shipping_charge)
            print(t)

            client = razorpay.Client(auth = (settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
            payment = client.order.create({'amount': t * 100, 'currency': 'INR', 'payment_capture': 1})
            print("----",payment)
            
            context = {
                    'payment': payment,
                }
                
            print("=======================",context)
                
            return render(request,"checkout.html",{'cart':cart,'net_price':net_price,'t':t,'shipping_charge':shipping_charge,'user':user,'order':order,'context':context})
        except:
            return redirect("index")
    else:
        return render(request,"checkout.html")

@never_cache
def success(request):
    try:
        user=User.objects.get(email=request.session['email'])
        cart=Cart.objects.filter(user=user,payment_status=False)

        for i in cart:
            i.payment_status=True
            i.save()
        return render(request,"success.html",{'cart':cart})
    except:
        return redirect("index")

@never_cache
def myorder(request):
    try:
        user=User.objects.get(email=request.session['email'])
        cart=Cart.objects.filter(user=user,payment_status=True)
        return render(request,"myorder.html",{'cart':cart})
    except:
        return redirect("index")
    
