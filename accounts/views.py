from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.

def login_view(request):
	next_redirect = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		next_redirect = request.POST.get('next')
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		if next_redirect != '':
			return redirect(next_redirect)
		return redirect('books:all')
	context = {'form':form, 'next':next_redirect}
	return render(request, 'accounts/login_form.html', context)


def register_view(request):
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		return redirect('books:all')

	context = {'form':form}
	return render(request, 'accounts/registration_form.html', context)

@login_required
def logout_view(request):
	logout(request)
	return redirect('books:all')