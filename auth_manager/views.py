from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']
        print(f'Username: {username}')
        user = authenticate(username=username, password=password)

        # redirect unauthenticated users somewhere
        # TODO understand how django.contrib.messages works
        if user is None:
            messages.error(request, "Bad Credentials!!")
            return redirect('auth/signin')

        # Successfully Authenticated Users
        login(request, user)
        request.session['user_id'] = user.id
        request.session['user_name'] = user.username
        request.session['email'] = user.email
        request.session['last_name'] = user.last_name

        # TODO what does reverse function do?
        profile_url = 'profile_manager:view_profile'
        return redirect(profile_url)

    return render(request, "auth/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    # TODO Successful sign-out should be redirected to login screen
    return redirect("auth_manager:signin")
