from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth, User
from .forms import FeedbackForm
from .models import Comment, details
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# from .models import Post
# from .forms import CommentForm
from django.shortcuts import render


def registration(request):
    form= CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')     
    context={'registerform':form}
    return render(request,'books/registration.html',context=context)

def user_login(request):
    form= LoginForm()
    if request.method== 'POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username,password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("home")
        # else:
        #      return redirect("registration")
        # else:
        #     form=LoginForm()
    
    
    context={'loginform':form}
            
    return render(request,'books/login.html',context=context)

@login_required
def home(request):
     books = details.objects.all()
     context = {'books': books,'name':request.user.username}
     return render(request,'books/index.html',context=context)

@login_required
def bookdetail(request, id):
    
     book= details.objects.get(id=id)

     return render(request, 'bookdetails.html',{'book': book})


@login_required
def dashboard(request):
    
    return render(request,'books/dashboard.html')

@login_required
def userreviews(request):
	feedbacks=Comment.objects.all()#fetches all feedback from table
	return render(request,'books/userreviews.html',{'feedbacks':feedbacks})

