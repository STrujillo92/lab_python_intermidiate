from django.shortcuts import render, redirect

# Create your views here.
def owner_list(request):
    #data_context={
     #   'nombre': 'Katty',
      #  'edad': 26,
       # 'pais':'Perú'
    #}
    data_context=[
        {'nombre': 'Katty Lopez',
         'edad': 26,
         'pais':'Perú',
         'dni':'23231212',
         'vigente':True,
         'pokemons': [
             {'nombre_p': 'charizard',
              'ataques': ['ataque1-ch','ataque2-ch','ataque3-ch','ataque4-ch']
              }
         ]},
        {'nombre': 'Benito Sanchez',
         'edad': 22,
         'pais':'España',
         'dni': '45452323',
         'vigente' : False },
        {'nombre': 'Marianela Rivera',
         'edad': 18,
         'pais':'Brasil',
         'dni': '78781212',
         'vigente' : False },
        {'nombre': 'Lucia Falconi',
         'edad': 15,
         'pais': 'Marruecos',
         'dni': '56562323',
         'vigente' : True }
    ]
    return render(request, 'owner/owner_list.html',context={'data':data_context})

def owner_detail(request,id_owner):
    print('ID Owner: {}'.format(id_owner))

    return render(request, 'owner/owner_list.html',context={'data':id_owner})
