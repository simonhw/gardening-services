from django.shortcuts import render


def index_page(request):
    '''
    View that renders the index.html page.
    '''

    return render(
        request,
        "home/index.html"
    )