from django.shortcuts import render, get_object_or_404
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


def service_page(request, service_id):
    '''
    View that displays the details of an individual product.
    '''

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, "services/service_page.html", context)
