from django.shortcuts import render


def index_page(request):
    """ View that renders the index.html page """

    return render(
        request,
        "home/index.html"
    )


def test_500_error_page(request):
    """
    Method to raise an Exception and trigger the 500 error page
    """

    raise Exception("Testing the 500 error page")


def custom_500_error(request):
    """
    A custom view to handle internal server errors while also providing
    the user authentication status in the context.
    """

    context = {
        'user': getattr(request, 'user', None)
    }

    return render(
        request, '500.html', context, status=500
    )
