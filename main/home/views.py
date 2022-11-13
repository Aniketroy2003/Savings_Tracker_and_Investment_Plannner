from django.shortcuts import render
from .models import Expense
# from .model import *
# Create your views here.
def home(request):
    if request.method=='POST':
        item = request.POST['item']
        monthly_expense = request.POST['monthly_expense']
        data = Expense(item=item,monthly_expense=monthly_expense)
        data.save()
    data = Expense.objects.all()
    print(data)
    ex = 0 
    for i in data:
        print(i.monthly_expense)
        ex = ex + int(i.monthly_expense)
    print(ex)
        
    updated_data = data.reverse()[::-1]


    return render(request,'index.html',{'data':updated_data,'ex':ex})

# def expense(request):
    
    # return render(request,'index.html',updated_data)

def invest(request):
    return render(request,'investment.html')


def sip(request):
    return render(request,'sip.html')