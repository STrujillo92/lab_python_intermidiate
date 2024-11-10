from django.shortcuts import render

# Create your views here.
def owner_list(request):
    data_context={
        'nombre': 'Katty'
    }

    return render(request, 'owner/owner_list.html',context={'data':data_context})