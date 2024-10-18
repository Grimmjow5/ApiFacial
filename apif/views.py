from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def indexLogin(request):
  return render(request, 'login.html')



def controlUser(request):
  return render(request, 'controlUser.html')
