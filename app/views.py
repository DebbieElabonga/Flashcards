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
