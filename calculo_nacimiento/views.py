from django.shortcuts import render
from django.http import HttpResponse, request

def dia_de_la_semana(dd, mm, aaaa):
    a = int((14 - mm) / 12)
    y = aaaa - a
    m = int(mm + (12 * a) - 2)
    d = int(dd + y + int(y/4) - int(y/100) + int(y/400)+((31*m) / 12)) % 7
    return d


def nombre_de_dia(numero_dia):
    return ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"][numero_dia]


def dia_semana(request,date):
	arreglo_fecha = date.split("-")
	dia     = dia_de_la_semana(int(arreglo_fecha[2]),int(arreglo_fecha[1]),int(arreglo_fecha[0]))
	nombre_dia  = nombre_de_dia(dia)
	print(nombre_dia)
	context = {"dia":arreglo_fecha,"nombre_dia":nombre_dia}
	return render(request,template_name="calculo_nacimiento/index.html", context=context)