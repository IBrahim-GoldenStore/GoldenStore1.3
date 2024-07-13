from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate,logout,login  # importation des fonction de connexion,deconnexion et verification
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from random import randint

# Create your views here.

def connexion(request):

    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        e_mail= request.POST['email']

        user= authenticate(username= username,passwords= password, email= e_mail)
        if user is not None:
            login(request, user)
            return redirect('store:index')
        else:
            messages.info(request, "Données incorrect")
    form= Connectform()

    return render(request,'account/connexion.html', {'form': form})

 
def deconnexion(request):
    user= logout(request)
    return redirect('store:index')


def compte(request):
    if request.method == 'POST':
        form= Userform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'account/success.html',{})
    else:
        form = Userform()
    
    return render(request, 'account/account.html',{'form': form,})
@login_required
def contacts(request):
    message= Messages_site.objects.all()
    avis=[]
    for i in range(0,11):
        if i < len(message):
            avis.append(message[i])
    if request.method == "POST":
        form_c = Message(request.POST)
        if form_c.is_valid():
            user= request.user
            name= user.username
            e_mail= user.email
            contenu= form_c.cleaned_data['message']
            message_base= Messages_site.objects.create(nom= name.capitalize(), e_mails= e_mail, message= contenu)
            message_base.save()
            return redirect('store:index')
    else:
        form_c= Message()

    return render(request, 'account/nos_contact.html',{"form": form_c,'avis':avis})

