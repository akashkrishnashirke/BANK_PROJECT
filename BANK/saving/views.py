from django.shortcuts import render

# Create your views here.
def show_saving(request):
    return render(request,'saving/saving.html',{'hi':'hi'})

def home(requeat):
    return render(requeat,'saving/home.html')