from django.http import HttpResponse

def bienvenida (request):
    return HttpResponse("Bienvenido Lunes 6 mayo")

def calcula_edad (request,edad):
    if edad >=18:
        categoria="Mayor o igual a 18"
    else:
        categoria="menor de edad"    
    result ="<h1> La edad es %s </h1>" %categoria
    return HttpResponse(result)

def situacion (request,edad2, edad3):
    if edad2 >0 and edad >0 :
        estado="Ambos son positivos"
    else:
        estado="son negativos"    
    result ="<h1> La edad es %s </h1>" %categoria
    return HttpResponse(result)