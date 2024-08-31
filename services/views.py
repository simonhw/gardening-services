from django.shortcuts import render
from .models import Service

def all_services(request):
    '''
    View that displays all services on offer
    '''

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, "services/services.html", context)