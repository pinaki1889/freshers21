from django.shortcuts import render
from .models import Confession
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=="POST":
        confession=Confession()
        name=request.POST.get('name')
        subject=request.POST.get('subject')

        confession.name=name
        confession.subject=subject
        confession.save()
        return HttpResponse("<h1>Thanks for your Secret confession</h1>")

    return render(request,'index.html')