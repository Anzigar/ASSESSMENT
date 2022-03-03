from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import *
from django.contrib.auth.hashers import make_password
from .models import *
from django.contrib.auth.models import User, auth
from .models import *


# Create your views here.
def index(request):
    u = Users.objects.all().count
    p = Plan.objects.all().count
    e = Expenses.objects.all().count
    context = {'u':u,'p':p,'e':e}
    
    return render(request, 'index.html',context)

def main(request):
    return render(request, 'main.html')

def manageuser(request):
    user = Users.objects.all()

    return render(request, 'manageuser.html',{'user':user})

def adduser(request):

    user = User()
    users=Users()
    if request.method == 'POST':
        firstname = request.POST['fname']
        middlename = request.POST['Mname']
        lastname = request.POST['lname']
        username = request.POST['username']
        address = request.POST['address']
        phonenumber=request.POST['phonenumber']
        password1 = "12345"
        email = request.POST['email']
        user.first_name = firstname
        users.middlename= middlename
        user.last_name=lastname
        user.username=username
        users.address=address
        users.phonenumber=phonenumber
        user.password = make_password(password1)
        user.email = email
        user.save()
        users.user=user
        users.save()

        return redirect('/manageuser')


    return render(request, 'adduser.html')


def edituser(request,pk):
    user = Users.objects.filter(user_id=pk)

    if request.method == 'POST':
        firstname = request.POST['fname']
        middle_name = request.POST['Mname']
        last_name = request.POST['lname']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        email = request.POST['email']


        User.objects.filter(id=pk).update(first_name=firstname, last_name=last_name, email=email)
        Users.objects.filter(user_id=pk).update(address=address, middle_name=middle_name, phonenumber=phonenumber)
        messages.success(request, 'Successfully User edited')
        return redirect('manageuser')

    return  render(request, 'edituser.html', {'user': user})

#@login_required(login_url="/login")
def deleteuser(request,pk):
    us= User.objects.get(id=pk)
    us.delete()
    return redirect('/manageuser')

def addproject(request):
    user = Plan()
    if request.method == 'POST':
        name1 = request.POST['name1']
        name2 = request.POST['name2']
        price = request.POST['price']

        user.plan_amount =price
        user.plan_details =name2
        user.plan_name=name1
        user.save()
        return redirect('/manageproject')

    return render(request, 'addproject.html')

def deleteproject(request,pk):
    us= Plan.objects.get(plan_id=pk)
    us.delete()
    return redirect('/manageproject')

def addexp(request):
    exp = Expenses()
    if request.method == 'POST':
        txt = request.POST['txt']
        #expensess= request.POST['expenses']
        amount =request.POST['amount']

        exp.expenses_amount = amount
        exp.expenses_name=txt
        #exp.expenses_details=expensess

        exp.save()
        return redirect('/manageexp')

    return render(request, 'addexp.html')

def manageproject(request):
    plan = Plan.objects.all()
    
    return render(request, 'manageproject.html', {'plan':plan})

def manageexp(request):
    exp = Expenses.objects.all()
    
    return render(request, 'manageexp.html', {'exp':exp})

# def editproject(request):
    

def profit(request):
    profit = Income.objects.all()
    profit.save()
    return render(request, 'profit.html')



def report(request):
    return render(request, 'report.html')

def expensesreport(request):
    return render(request, 'expensesreport.html')

def signup(request):
    user = User.objects.all()
   
    if request.method == 'POST':
        username = request.POST['fname']
        middlename = request.POST['Mname']
        lastname = request.POST['lname']
        address = request.POST['address']
        password1 = request.POST['password1']
        email = request.POST['email']        
        user.username = username
        user.middlename= middlename
        user.lastname=lastname
        user.address=address
        user.password = make_password(password1)
        user.email = email
        user.save()
        messages.info(request, "Account created Successfully ")
        return redirect('/index')
    else:
        #messages.info(request, "password does not match")
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect( '/index')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/login')

def managerole(request):
       
      group = Group.objects.all()
      r = Permission.objects.all()
      return render(request,'managerole.html',{'r':r,'group':group})


def addrole(request):
   p = Group()
   group = Group.objects.all()
   r = Permission.objects.all()
   if request.method == "POST":
      name = request.POST.get("name")
      permission = [x.name for x in Permission.objects.all()]
      s_id = []
      p.name=name
      for x in permission:
             s_id.append(int(request.POST.get(x))) if request.POST.get(x) else print("")
      p.save()
      for s in s_id:
           p.permissions.add(Permission.objects.get(id=s))   
      return redirect('/managerole')  
   return render(request,'addrole.html',{'r':r, 'group':group})

def editrole(request,pk):

   p = Permission.objects.all()
   r = Group.objects.filter(id=pk)
   y=Group.objects.get(id=pk)
   if request.method == 'POST':
    name = request.POST.get('name')
    
             
    for j in Permission.objects.all():
              y.permissions.remove(j.id) 
      
      
    permission = [x.name for x in Permission.objects.all()]
     
    s_id = []
    Group.objects.filter(id=pk).update(name=name)
    for x in permission:
             s_id.append(int(request.POST.get(x))) if request.POST.get(x) else print("")
    r=Group.objects.filter(id=pk).update(name=name)
      
    for s in s_id:
           y.permissions.add(Permission.objects.get(id=s))  
    return redirect('/managerole')
           
   return render(request,'editrole.html',{'r':r,'p':p})

def grantRole(request,pk):
    group=Group.objects.all()
             
    # d=Admins.objects.all()
    u = User.objects.get(id=pk)
    d=Users.objects.filter(id=pk)
    p = User.objects.get(id=pk)
    r = Group.objects.filter(id=pk)
    
    if request.method == 'POST':
        
      for i in Group.objects.all():
             u.groups.remove(i.id)
             
      permission = [x.name for x in Group.objects.all()]
      s_id = []
      
      for x in permission:
             s_id.append(int(request.POST.get(x))) if request.POST.get(x) else print("")
      
      for s in s_id:
           u.groups.add(Group.objects.get(id=s))  
      return redirect('/manageuser')
    return render(request, 'grantRole.html',{'group':group,'d':d,'u':u})

def deleterole(request,pk):
    
    Group.objects.filter(id=pk).delete()
    
    return redirect('/managerole')

def trash(request):
    
    group=Users.objects.filter(is_deleted='True')                  
    
    
    return render(request, 'trash.html',{'group':group})   