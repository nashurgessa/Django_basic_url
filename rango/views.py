from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Yeroo client index site galuu, httpresponse ("Rango Says hey there partner")
# takes => HttpRequest
# return => HttpResponse
def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake"}
    return render(request, 'rango/index.html', context=context_dict)