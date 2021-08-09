from django.shortcuts import render

# Create your views here. 
from django.views.generic import View 

from app.models import *

class Home(View):
    def get(self,request):
        return render(request,'app/home.html')