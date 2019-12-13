from django.http.response import JsonResponse
import discogs_client

discogs_api = discogs_client.Client('my_user_agent/1.0', user_token='iveLOjvMtgyHUUCuyAzElYGLTuWzBeyiOhpjAEYA')


def index(request):
    results = discogs_api.search('Sell', genre='Blues', format='Vinyl',
                                 currency='GBP', price='5to10', year='1991')
    all_dicts = []
    print(len(results))
    for result in results:
        dict1 = {}
        dict1['title'] = result.title
        all_dicts.append(dict1)
    return JsonResponse(all_dicts, safe=False)
