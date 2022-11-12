from django.shortcuts import render
from django.http import HttpResponse
from contacto.forms import Contacto


# Create your views here.

def mensaje_contacto(request):

    if request.method=="POST":
        contact_form = Contacto(request.POST)

        if contact_form.is_valid():
            obtener_datos = contact_form.cleaned_data
            return HttpResponse(str(obtener_datos))

    else:

        contact_form = Contacto()
        return render (request, "contact_form.html", {"form": contact_form})
