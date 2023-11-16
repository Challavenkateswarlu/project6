from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dravid(request):
    return render(request,'dravid.html')
def zaheer(request):
    return HttpResponse('<h1>wicket taker</h1>')