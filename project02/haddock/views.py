from django.contrib.auth.models import User
from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.contrib import auth
from django.urls import reverse
from .models import Incidente, Criticidade,Areas,UserData,Registro
from django.utils import timezone
import requests
import os
from twilio.rest import Client


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def index(request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        template=loader.get_template('haddock/index.html')
        context={}
    else:
        template = loader.get_template('haddock/indexdesktop.html') 
        context = { }
    return HttpResponse(template.render(context, request))

def telaregistro(request):
    template = loader.get_template('haddock/telaregistro.html')
    incidente=Incidente.objects.order_by('-id')
    criticidade=Criticidade.objects.order_by('-id')
    context = { 'incidente':incidente, 'criticidade':criticidade}
    a=request.user.get_username




    return HttpResponse(template.render(context, request))

def equipe(request):
    template = loader.get_template('haddock/equipe.html') 
    context = { }
    return HttpResponse(template.render(context, request))

def how(request):
    template = loader.get_template('haddock/how.html') 
    context = { }
    return HttpResponse(template.render(context, request))

def what(request):
    template = loader.get_template('haddock/what.html') 
    context = { }
    return HttpResponse(template.render(context, request))


def login_view(request):
    user=auth.authenticate(username='hackathon',password='password')
    auth.login(request,user)
    return HttpResponseRedirect(reverse('haddock:telaregistro'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('haddock:index'))

def requisicao(request): 
    try:
        selected_incidente = Incidente.objects.get(pk=request.POST['respincidente'])
        selected_criticidade = Criticidade.objects.get(pk=request.POST['respcriticidade'])
    except (KeyError, Incidente.DoesNotExist):
        return HttpResponse(template.render(context, request))
    else:
        registrar=Registro(resolvido="False", criador=request.user.get_username, pub_date=timezone.now(),area=" ", localizacao=" ",criticidade=selected_criticidade.nivel,incidente=selected_incidente.tipo,nivel=0)
        registrar.save()

        a=selected_incidente.tipo
        b=selected_criticidade.nivel
        c=" "

        headers = {'content-type':'application/json','Authorization':'Bearer af8df04726988bf2eca0e0a1a763fa283279bb1f1d1b2f4fe2dd0d122eb265f6'}
        data = {'from':'0x557F81f0BD7f8cA83e06811f8a90F4A6b9a3Ca20','to':'0x557F81f0BD7f8cA83e06811f8a90F4A6b9a3Ca20','value':0,'data':'incident:{incidente},criticidade:{crit},localizacao:{loc}'.format(incidente=a,crit=b,loc=c),'pk':'0xd4ae53f91d65f7c2fa07a8cb8afba18e48b3160dcf9fb386ac9019268839123a','estimatedGas':'false'}

        request = requests.post('http://portohack.rbiblockchain.io/stcpconnector/registerdata', headers=headers,json=data)

        # Your Account SID from twilio.com/console
        account_sid = "AC293eb75e040f4b3b7bac23a6a23b255b"
        # Your Auth Token from twilio.com/console
        auth_token  = "1dd041ca5e10cb4f41912a44596ba2c0"

        client = Client(account_sid, auth_token)

        # this is the Twilio sandbox testing number
        from_whatsapp_number='whatsapp:+14155238886'
        # replace this number with your own WhatsApp Messaging number
        to_whatsapp_number='whatsapp:+5511963964336'

        client.messages.create(body='Verificar possível incidência de: '+a+'; Nível: '+str(b)+' ; Area 3',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

    return HttpResponseRedirect(reverse('haddock:index'))

