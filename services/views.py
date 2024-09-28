from django.shortcuts import render, get_object_or_404
from .models import Service, Category


def all_services(request):
    '''
    View that displays all services on offer
    '''

    services = Service.objects.all().order_by('pk')
    categories = None
    category_heading = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            services = services.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            category_heading = True

    context = {
        'services': services,
        'current_categories': categories,
        'category_heading': category_heading,
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
