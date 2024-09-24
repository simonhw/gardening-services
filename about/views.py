from django.shortcuts import render


def about_page(request):
    """
    View that renders the about.html page.
    """

    return render(request, 'about/about.html')