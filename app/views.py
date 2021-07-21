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
from app.models import Card, Subject
from django.shortcuts import render,redirect
from .forms import CardForm

# Create your views here.

def index(request):
    cards=Card.objects.all()

    return render(request,'index.html',{'cards':cards})

def createcard(request):
    subjects=Subject.objects.all()
    if request.method == "POST":
        data=request.POST

        if data['subject']!='none':
            subject=Subject.objects.get(id=data['subject'])
        elif data['subject_new']!='':
            subject,created=Subject.objects.get_or_create(name=data['subject_new'])
        else:
            subject=None
        cards=Card.objects.create(
            subject=subject,
            title=data['title'],
            note=data['note'],

        )
        return redirect('index')
    context={'subjects':subjects}

    #     form=CardForm(data=request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         obj=form.instance
    #     return redirect('index')
    # else:
    #     form=CardForm()
    #     card=Card.objects.all()
    return render(request,"create-card.html",context)
