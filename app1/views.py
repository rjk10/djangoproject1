from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def django(request):
    return HttpResponse('<h1><marquee>python framework</marquee></h1>')
def aws(request):
    return HttpResponse('<h1><marquee>amazon web service</marquee></h1>')

