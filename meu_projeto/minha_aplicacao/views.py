from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    nome=""
    if request.method == "POST":
        nome= request.POST.get("nome", "")
    return render(request, "minha_aplicacao\index.html",{"nome": nome})