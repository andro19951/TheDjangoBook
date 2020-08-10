from django.shortcuts import render

# Create your views here.
def index(response):
    return render(request, 'airlines/index.html',{})