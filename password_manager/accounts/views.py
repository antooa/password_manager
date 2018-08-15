from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import *
import pdb
# Create your views here.
def login(request):
    if request.POST.get('submit') == 'sign_in':
        form = login_form(data=request.POST)
        pdb.set_trace()
        return redirect('/account')
        #if form.is_valid():

         #   return HttpResponseRedirect('/account')

    elif request.POST.get('submit') == 'sign_up':
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account')
    else:
        sign_in = login_form()
        sign_up = register_form()
        return render(request, 'login.html', {'login_form':sign_in, 'signup_form': sign_up})

def account(request):
    return HttpResponse('Account')