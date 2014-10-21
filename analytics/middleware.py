from ipware.ip import get_real_ip
from django.conf import settings
import requests
from models import Page, Location, View



class LocationMiddleware(object):
    def process_request(self, request):
        # Get the IP Address of this request
        ip = get_real_ip(request)

        # If we didn't get an IP Address and we're developing locally,
        # make an API call to get our IP Address.
        if ip is None and settings.DEBUG:
            ip = requests.get('http://icanhazip.com/').text
            if ip is not None:
                response = requests.get('http://ipinfo.io/{}/json'.format(ip))
                if response.status_code == 200:
                    request.location = response.json()
                    # Split out the lat and long from the location
                    request.location['latitude'], request.location['longitude'] = request.location['loc'].split(',')

            request.ip = ip

class PageViewMiddleware(object):
    def process_request(self, request):
        page, created = Page.objects.get_or_create(url=request.META['PATH_INFO'])
        location, created = Location.objects.get_or_create(country=request.location['country'],
                                                           region=request.location['region'],
                                                           city=request.location['city'])
        view, created = View.objects.get_or_create(page=page,
                                   ip_address=request.ip,
                                   location=location,
                                   latitude=request.location['latitude'],
                                   longitude=request.location['longitude'])
        print page, location, view

