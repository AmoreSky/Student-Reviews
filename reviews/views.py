from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from .forms import ReviewForm, SignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def reviews(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            # print(form.cleaned_data)\
            form.save( )
            return redirect(reverse('reviews:thank_you'))

    else:
        form = ReviewForm()
    return render(request,'reviews/reviews.html', context={'form':form})

def thank_you(request):
    return render(request, 'reviews/thank_you.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form)
        if form.is_valid():
            user = form.save()
            user.full_name = form.cleaned_data.get('full_name')
            user.matric_number = form.cleaned_data.get('matric_number')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            # return redirect(reverse('reviews:reviews'))
            return redirect(reverse('reviews:reviews'))
        else:
            print(form.errors)
            return render(request, 'reviews/signup.html', {'form': form})

    else:
        form = SignUpForm()
        return render(request, 'reviews/signup.html', {'form': form})
