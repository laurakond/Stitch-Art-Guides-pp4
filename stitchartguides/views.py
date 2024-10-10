from django.shortcuts import render


def error_400(request, exception):
    """Function that renders error 400 bad request."""
    return render(
        request,
        "errors/400.html",
        status=400
    )


def error_403(request, exception):
    """Function that renders error 403 access forbidden."""
    return render(
        request,
        "errors/403.html",
        status=403
    )


def error_404(request, exception):
    """Function that renders error 404 page not found."""
    return render(
        request,
        "errors/404.html",
        status=404
    )


def error_500(request):
    """Function that renders error 500 internal server error."""
    return render(
        request,
        "errors/500.html",
        status=500
    )
