from app.models import Card
from django.shortcuts import render,redirect
from .forms import CardForm

# Create your views here.

def index(request):
    cards=Card.objects.all()

    return render(request,'index.html',{'cards':cards})

def createcard(request):
    if request.method == "POST":

        form=CardForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
        return redirect('index')
    else:
        form=CardForm()
        card=Card.objects.all()
    return render(request,"create-card.html",{"form":form,'card':card})
