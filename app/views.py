from app.models import Card, Subject
from django.shortcuts import render,redirect
from .forms import CardForm , UserCreationForm
from django.contrib.auth import login, authenticate
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
 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})