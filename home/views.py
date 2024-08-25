from django.shortcuts import render
from django.views import generic


def index_page(request):
    '''
    View that renders the index.html page.
    '''

    return render(
        request,
        "home/index.html"
    )