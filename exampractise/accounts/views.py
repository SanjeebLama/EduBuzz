from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def test(request):
    return render(request, 'accounts/test.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("insideAuth")
        else:
            messages.info(request, 'invalid credentials')
            return redirect("login")
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'user created')
                return redirect('/accounts/login')
        else:
            messages.info(request, 'password not matching')
        return redirect('/accounts/register')

    else:
        return render(request, 'accounts/register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


# Authentication in Web requests
# insideAuth type garda ne page kholdaina untill you login
def insideAuth(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/insideAuth.html')

    else:
        return render(request, 'accounts/login.html')
