from django.db.models import F, Q
from django.shortcuts import render, redirect

from owner.models import Owner
from owner.forms import OwnerForm

from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def owner_list(request):
    #data_context={
     #   'nombre': 'Katty',
      #  'edad': 26,
       # 'pais':'Perú'
    #}
    # data_context=[
    #     {'nombre': 'Katty Lopez',
    #      'edad': 26,
    #      'pais':'Perú',
    #      'dni':'23231212',
    #      'vigente':True,
    #      'pokemons': [
    #          {'nombre_p': 'charizard',
    #           'ataques': ['ataque1-ch','ataque2-ch','ataque3-ch','ataque4-ch']
    #           }
    #      ]},
    #     {'nombre': 'Benito Sanchez',
    #      'edad': 22,
    #      'pais':'España',
    #      'dni': '45452323',
    #      'vigente' : False },
    #     {'nombre': 'Marianela Rivera',
    #      'edad': 18,
    #      'pais':'Brasil',
    #      'dni': '78781212',
    #      'vigente' : False },
    #     {'nombre': 'Lucia Falconi',
    #      'edad': 15,
    #      'pais': 'Marruecos',
    #      'dni': '56562323',
    #      'vigente' : True }
    # ]

    '''Crear un objeto de una tabla de la BD'''
    #p = Owner(nombre='Luis Mejia',edad=22,dni='12312312',pais='España',vigente=True)
    #p.save()

    '''Obtener todos los elementos de una tabla de la BD'''
    #data_context=Owner.objects.all()

    '''Filtración de datos: filter()'''
    #data_context=Owner.objects.filter(nombre='Steve')

    '''Filtración de datos con AND de SQL: filter( , )'''
    #data_context=Owner.objects.filter(nombre='Lidia',edad=23)

    '''Filtración de datos más preciso: con __contains'''
    #data_context=Owner.objects.filter(nombre__contains='Luis')

    '''Filtración de datos más preciso: con __endswith'''
    #data_context=Owner.objects.filter(nombre__endswith='ia')

    '''Obtener un solo objeto de la tabla de BD'''
    #data_context=Owner.objects.get(dni='07612311')

    '''Ordenar por cualquier atributo o campos en la tabla'''
    #data_context=Owner.objects.order_by('nombre')
    #data_context=Owner.objects.order_by('-edad')

    '''Ordenar concatenando diferentes métodos ORM's '''
    #data_context=Owner.objects.filter(nombre__contains='Luis').order_by('-edad')

    '''Acortar datos: obtener un rango de registros de una tabla de la BD'''
    #data_context=Owner.objects.all()[0:3]

    '''Eliminar un dato especificamente'''
    # try:
    #     data_context=Owner.objects.get(id=4)
    #     data_context.delete()
    # except Owner.DoesNotExist:
    #     data_context=[]

    '''Actualización de datos en la BD a un cierto grupo de datos o un solo registro'''
    #Owner.objects.filter(pais__startswith='Es').update(edad=34)

    data_context=Owner.objects.all()

    '''Utilizando F expressions'''
    #Owner.objects.filter(edad=25).update(edad=F('edad') + 15)
    #p = Owner(nombre='Gloria',edad=22,dni='74561238',pais='peru',vigente=False)
    #p.save()
    #Owner.objects.filter(pais='peru',edad__lt=25).update(edad=F('edad') + 10)

    '''Consultas complejas'''
    #query = Q(pais__startswith='pe') | Q(pais__startswith='co')
    #data_context=Owner.objects.filter(query)

    '''Negar Q'''
    #query = Q(pais__startswith='pe') & ~Q(edad=30)
    #data_context=Owner.objects.filter(query)
    #data_context=Owner.objects.filter(query,nombre__endswith='na')

    '''Error de consulta'''
    #query = Q(pais__startswith='pe') & ~Q(edad=30)
    #data_context = Owner.objects.filter(nombre__endswith='na',query )

    #p = Owner(nombre='Esteban', edad=29, dni='45456262', pais='España', vigente=False)
    #p.save()
    #p = Owner(nombre='Lucrecia', edad=29, dni='99784523', pais='peru', vigente=True)
    #p.save()

    query = (Q(pais__endswith='ña') | Q(pais__startswith='pe')) & Q(edad=29)
    data_context=Owner.objects.filter(query)

    return render(request, 'owner/owner_list.html',context={'data':data_context})


def owner_detail(request,id_owner):
    print('ID Owner: {}'.format(id_owner))

    return render(request, 'owner/owner_list.html',context={'data':id_owner})

def owner_search(request):
    query = request.GET.get('q','')
    #verificar con el terminal, que el dato pedido llega al form
    print('Query: {}'.format(query))

    results = (
        Q(nombre__icontains=query)
    )

    data_context=Owner.objects.filter(results)
    #verificando con el terminal
    print('data_context: {}'.format(data_context))

    return render(request, 'owner/owner_search.html',context={'data':data_context,'query':query})

def owner_create(request):
    print('Request: {}'.format(request.POST))
    form = OwnerForm(request.POST)

    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        edad = form.cleaned_data['edad']
        pais = form.cleaned_data['pais']

        form.save()
        # para que después de guardar envie a otra plantilla
        return redirect('owner_details')
    else:
        form = OwnerForm()

    return render(request,'owner/owner_create.html',{'form':form})

def owner_details(request):
    data_context=Owner.objects.all()
    return render(request, 'owner/owner_details.html',context={'data':data_context})

def owner_delete(request,id_owner):
    print('ID Owner: {}'.format(id_owner))
    owner = Owner.objects.get(id=id_owner)
    owner.delete()

    return redirect('owner_details')

def owner_edit(request,id_owner):
    owner = Owner.objects.get(id=id_owner)

    form = OwnerForm(initial={'nombre':owner.nombre,'edad':owner.edad,'pais':owner.pais,'dni':owner.dni})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_details')


    return render(request,'owner/owner_edit.html',{'form':form})

'''Vistas basadas en clases'''
'''ListView, CreateView, UpdateView, DeleteView'''

class OwnerList(ListView):
    model = Owner
    template_name = 'owner/owner_list_vc.html'

class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = "owner/owner_create.html"
    success_url = reverse_lazy('owner_list_vbc.html')

class OwnerUpdate(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_update_vc.html'

class OwnerDelete(DeleteView):
    model = Owner
    success_url = reverse_lazy('owner_list_vbc')
    template_name = 'owner/owner_confirm_delete.html'