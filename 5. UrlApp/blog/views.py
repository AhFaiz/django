from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog.html')

def recent(request):
    return HttpResponse("<h1> This is Recent Blog </h1>")