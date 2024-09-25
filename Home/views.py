from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Game, game1
import razorpay
from .models import game1
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    return render(request,'index.html')

def crud(request):
    gm = Game.objects.all()
    context = {
        'gm':gm
    }
    return render(request,'crud.html',context)

def Add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        payment = request.POST.get('payment')

        gm = Game(
            name = name,
            category = category,
            price = price,
            payment = payment,
        )

        gm.save()
        return redirect('index')
    
    return render(request,'crud.html')

def Edit(request):
    gm = Game.objects.all()

    context = {
        'gm':gm
    }
    return redirect(request,'crud.html',context)

def Update(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        payment = request.POST.get('payment')

        gm = Game(
            id = id,
            name = name,
            category = category,
            price = price,
            payment = payment,
        )
        gm.save()
        return redirect('index')
    return redirect(request,'crud.html')

    return redirect(request,'crud.html')

def Delete(request,id):
    gm = Game.objects.filter(id=id)
    gm.delete()
    context = {
        'gm':gm,
    }
    return redirect('index')


def payment(request):
    if request.method=="POST":
        name=request.POST.get("name")
        amount=int(request.POST.get("amount")) * 100
        #email=request.POST.get("email")
        client = razorpay.Client(auth=('rzp_test_iZ4vwZ4XJfBYcT', 'L5J6tis4PKzBJz6izYVAvSpL'))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        print(payment)
        Game=game1(name=name,amount=amount,Payment_id=payment['id'])
        Game.save()
        #return render(request,'payment.html')
        return render(request,"payment2.html",{'payment':payment})
        #return redirect('index')
       # print(name)
        # print(amount)
    return render(request,"payment2.html")


 
