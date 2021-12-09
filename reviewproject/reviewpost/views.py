from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import ReviewModel
from django.shortcuts import render , redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def columnview(request):
    if request.method == 'POST':
        return redirect('login')
    else:
        return render(request, 'login.html', {})

@login_required
def listview(request):
    object_list = ReviewModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username_data')
        password = request.POST.get('password_data')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            print("successfully logined")
            return redirect('list')
        else:
            print("miss")
            return redirect('login')
            
    else:
        print("?")
        return render(request, 'login.html', {})
        

def logoutview(request):
    logout(request)
    return redirect('login')

def signupview(request):
    pass

def evaluationview(request, pk):
    post = ReviewModel.objects.get(pk=pk)
    print(post.useful_num)
    post.useful_num = post.useful_num + 1
    print(post.useful_num)
    post.save()
    return redirect('list')

@login_required
def detailview(request, pk):
    object = ReviewModel.objects.get(pk = pk)
    return render(request, 'detail.html', {'object': object})

class CreateClass(CreateView):
    template_name = 'create.html'
    model = ReviewModel
    fields = ('author','title','content','product_image')
    success_url = reverse_lazy('list')
