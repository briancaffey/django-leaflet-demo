from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.

def login_view(request):

	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		messages.success(request, 'Welcome back, ' + str(request.user) + '!')
		print(next)
		if next:
			print(next)
			return redirect(next)
		return redirect('books:all')

	return render(request, 'accounts/login_form.html', {'form':form})


def register_view(request):
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		messages.success(request, 'Thanks for registering, ' + str(request.user.username) + '!')
		return redirect('books:all')
	context = {
		'form':form,
		}
	return render(request, 'accounts/registration_form.html', context)

@login_required
def logout_view(request):
	logout(request)
	messages.success(request, "You have successfully logged out.")
	return redirect('books:all')