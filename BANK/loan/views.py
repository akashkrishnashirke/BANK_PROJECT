from django.shortcuts import render,redirect
from .forms import LoanApplictionModelForm
import random
from .models import LoanApplicationModel

# Create your views here.
def thanks(request):
    reference_no= random_digit(1)
    md={'reference_no': reference_no}
    return render(request,'loan/responce.html',context=md)


def random_digit(n):
    num=range(111111111,999999999999)
    l=random.sample(num,n)   
    return str(l).strip('[]')

def show_loan(request):
    form=LoanApplictionModelForm()
    md={'form':form}


    if request.method=='POST':
        name=request.POST['name']
        inc=request.POST['income']
        mob=request.POST['mobileNo']
        addr=request.POST['address']
        if len(name)>5:
            reg=LoanApplicationModel(name=name,income=inc,mobileNo=mob,address=addr)
            reg.save()
            return thanks(request)
        else:
            return redirect('/show/')

        #form=LoanApplictionModelForm(request.POST)
        #if form.is_valid():


            #print(form.cleaned_data['name'])
            #form.save(commit=True)
            #name = request.POST['name']
            #print(name)
            #return thanks(request)


    return render(request,'loan/loan form.html',context=md)



def show_data(request):
    data=LoanApplicationModel.objects.all()

    return render(request,'loan/show data.html',{'data':data})



'''no changes dones by me'''
