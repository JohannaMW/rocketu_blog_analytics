from analytics.models import View, Page


def location(request):
    return {
        'location': request.location
    }

def analytics(request):
    return {
        'pages' : Page.objects.all()
    }
