from django.shortcuts import render

# Create your views here.
def homee(request):
    return render(request,"index.html")
def about(request):
    return render(request,"index.html")
def service(request):
    return render(request,"index.html")
def price(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"index.html")
