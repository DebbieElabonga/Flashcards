from django.shortcuts import render,redirect
from . models import Profile,Subject,Card
from . forms import ProfileForm
# Create your views here.


def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            redirect(request.path_info)
    else:
        form = ProfileForm(instance=request.user.profile)
    profile = Profile.objects.filter(user=user)
    cards = Card.objects.filter(user=user)
    return render(request,'profile.html',{"user":user,"profile":profile,"cards":cards,"form":form})