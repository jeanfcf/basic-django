from django.shortcuts import render

# Create your views here.


def index(request):
    context={
        'pj':' poli junior',
    }
    return render(request,'core/index.html',context)

def contatos(request):
    context={
        'jean': 'JEÂNUS',
        'na':'LJLJLAJSLSFLAFSLF',
    }
    return render(request,'core/contato.html',context)