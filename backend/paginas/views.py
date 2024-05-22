from django.shortcuts import render

def home (request):
    return render (request, 'home.html')

def contact (request):
    return render (request, 'contact.html')

def Over (request):
    return render (request, 'overSBWE.html')

def historie (request):
    return render (request, 'historie.html')

def atelier(request):
    return render (request, 'atelier.html')


#CC
def verhuurBK (request):
    return render (request, 'CC/verhuurBK.html')

def reserveringBK (request):
    return render (request, 'CC/reserveringBK.html' )

def beschikBK (request):
    return render (request, 'CC/Beschikbaarheid.html' )

def voorwaardenBK (request):
    return render (request, 'CC/voorwaardenBK.html' )

def impressieBK (request):
    return render (request, 'CC/impressieBK.html' )


#panden
def panden (request):   
    return render (request, 'panden/panden.html')

def gebouwBK (request):
    return render (request, 'panden/barthkapel.html' )

def gebouwLO (request):
    return render (request, 'panden/looyerstr.html' )


#post/ blog
def post_list (request):
    return render (request, 'post_list.html' )