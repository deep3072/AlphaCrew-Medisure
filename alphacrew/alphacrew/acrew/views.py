# Create your views here.

from django.shortcuts import render
from acrew.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import requests
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
# from .models import Question
# from .models import Course

# mydict = {}


def index(request):
    return render(request, "acrew/index.html")



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'acrew/registration.html',
                          {'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'acrew/login.html', {})


def contact(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/contact.html')


def nearby(request):
    return render(request, 'acrew/hos.html')

def diseases(request):
    return render(request, 'acrew/diseases.html')

def search(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('index'))
    response = requests.get('https://api.covid19api.com/summary').json()
    # print(response)
    return render(request, 'acrew/search.html', {'responses': response})
    # return HttpResponse("hello")


def about(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/about.html')


def exercise(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/exercise.html')


def corona(request):
    return render(request, 'acrew/corona.html')


def womenshealth(request):
    return render(request, 'acrew/womenshealth.html')


def flu(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/flu.html')


def symptoms(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/symptoms.html')


def flu(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/flu.html')


def cough(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/cough.html')


def fever(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/fever.html')


def jaundice(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/Jaundice.html')


def diabetes(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/diabetes.html')


def malaria(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/malaria.html')


def bloodpressure(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/bloodpressure.html')


def allergies(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/allergies.html')


def typhoid(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/typhoid.html')


def stomachache(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/stomachache.html')


def conjuctivitis(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/conjuctivitis.html')


def dengue(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'acrew/dengue.html')
