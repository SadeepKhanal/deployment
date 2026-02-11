from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth.hashers import check_password


def student_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get('password')
        print(username)

        try:
            student=Student.objects.get(username=username)
            if check_password(password,student.password):
                request.session['student_id']=student.id
                request.session['student_name']=student.name
                return redirect('dashboard')
            else:
                 return render(request,"session/login.html",{
                "error":"invalid password"
            })

        except:
            return render(request,"session/login.html",{
                "error":"not found"
            })

        
    return render(request,"session/login.html")

def student_dashboard(request):
    name=request.session.get("student_name")
    return render(request,"session/dashboard.html")
 
def student_logout(request):
    pass 