from django.shortcuts import render,redirect
from .models import Register,Login
from django.http import HttpResponse
# Create your views here.

def view(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        acc_no=request.POST['acc_no']
        name=request.POST['name']
        amount=int(request.POST['amount'])
        phone=request.POST['phone']
        password=request.POST['password']
        if amount<=1000:
            return render(request,'index.html',{'message':"The amount must be greater than 1000"})
        else:
         data=Register.objects.create(Acc_number=acc_no,Name=name,Amount=amount,Phone=phone)
         data.save()
         data1 =Login.objects.create(Acc_number=acc_no,Password=password)
         data1.save()
         return render(request,'login.html')
    else:
        return render(request, 'index.html')

def loginpage(request):
    return render(request,'login.html')

def login(request):
    if request.method=="POST":
        acc_no=request.POST['acc_no']
        password=request.POST['password']
        try:
            data=Login.objects.get(Acc_number=acc_no)
            if data.Password==password:
                request.session['id']=acc_no
                return redirect(details)
            else:
                return HttpResponse("password error")
        except Exception:
            return HttpResponse("account number error")
    else:
        return render(request, 'login.html')

def details(request):
    if 'id' in request.session:
        acc_no=request.session['id']
        if request.method =='GET':
            data=Register.objects.filter(Acc_number=acc_no).all()
            return render(request,'table.html',{'data':data})

def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(login)


def deposit(request):
   return render(request,'deposit.html')

def newdetails(request):
    if request.method == "POST":
        acc_no = request.POST['acc_no']
        deposit =int(request.POST['deposit'])
        data = Register.objects.get(Acc_number=acc_no)
        data.Amount += deposit
        data.save()
        context = {
            'msg': "The amount deposited succesfully"
        }
        return render(request, 'deposit.html',context)



def withdraw(request):
    return render(request,'withdraw.html')

def withdrawed(request):
    if request.method=="POST":
        acc_no=request.POST['acc_no']
        withdraw=int(request.POST['withdraw'])
        if withdraw % 100 ==0 or withdraw % 200==0 or withdraw % 500==0:
          data=Register.objects.get(Acc_number=acc_no)
          data.Amount-=withdraw
          data.save()
          context={
            'msg': "The amount withdrawn successfully"
          }
          return render(request,'withdraw.html',context)
        else:
            return render(request,'withdraw.html',{'note':"The amount is not a multiple of 100,200 or 500"})


