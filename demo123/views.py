from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactFrom,LoginForm
from .models import Student
def reg(request):
    if request.method=="POST":
        form=ContactFrom(request.POST)
        if form.is_valid():
            fname=request.POST.get('fname','')
            lname=request.POST.get('lname','')
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            email=request.POST.get('email','')
            mobile=request.POST.get('mobile','')
            person=Student(fname=fname,lname=lname,username=username,password=password,email=email,mobile=mobile)
            person.save()
            #return redirect('/#?')
            return HttpResponse("data inserted successfully")
    else:
        form=ContactFrom()
        return render(request,'reg.html',{'form':form})

def login(request):
    if request.method=="POST":
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            un=login_form.cleaned_data['username']
            pw=login_form.cleaned_data['password']
            dbuser=Student.objects.filter(username=un,password=pw)
            if not  dbuser:
                return render(request, 'login.html', {'login_form': login_form,'message':'invalid credentials'})
            else:
                return render(request, 'welcome.html', {'login_form': login_form, 'message': 'invalid credentials'})

    else:
        login_form=LoginForm()
        return render(request,'login.html',{'login_form':login_form})
