from django.shortcuts import render, redirect

# Create your views here.
def owner_list(request):
    #data_context={
     #   'nombre': 'Katty',
      #  'edad': 26,
       # 'pais':'Perú'
    #}
    data_context=[
        {'nombre': 'Katty',
         'edad': 26,
         'pais':'Perú'},
        {'nombre': 'Benito',
         'edad': 22,
         'pais':'España'},
        {'nombre': 'Marianela',
         'edad': 18,
         'pais':'Brasil'}
    ]
    return render(request, 'owner/owner_list.html',context={'data':data_context})

def owner_detail(request,id_owner):
    print('ID Owner: {}'.format(id_owner))

    return render(request, 'owner/owner_list.html',context={'data':id_owner})
