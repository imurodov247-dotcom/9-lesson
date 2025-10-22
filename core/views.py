from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from . models import Profile
from .forms import ProfileForm
from django.http import HttpResponseNotAllowed

# Create your views here.
def index(request):
    print(" view logikasi run boldi")
    return render(request,'core/index.html')

# class HelloView(View):
#     def get(self,request):
#         return HttpResponse("salom")
    
#     def post(self,request):
#         return HttpResponse("nimadur")
def create_profile(request):
    print("Ulandi")
    if request.method =="POST" and request.FILES["image"]:
        print("O'tdi")
        form = ProfileForm(request.POST, request.FILES['image'])
        print("obyekt olindi")
        if form.is_valid():
            form.save()
            return redirect("index")
        
    return HttpResponseNotAllowed(['POST'])

def profiles(request):
    profiles = Profile.objects.all()
    return render(request,"core/profiles.html",{"profiles":profiles})    

 