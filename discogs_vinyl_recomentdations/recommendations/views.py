# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.http import JsonResponse
import discogs_client

# discogs_api = discogs_client.Client('LorenaApplication/0.1')
discogs_api = discogs_client.Client('my_user_agent/1.0', user_token='iveLOjvMtgyHUUCuyAzElYGLTuWzBeyiOhpjAEYA')
# discogs_api.set_consumer_key('xgyLfCnLCnazoNhPtLAm', 'eWmpVjDdsTIWYDxoMjqdvRKajdsZcTrs')


def index(request):
    results = discogs_api.search('test', genre='Blues')
    print(results.page(1))
    return JsonResponse(list(results.page(1)), safe=False)
