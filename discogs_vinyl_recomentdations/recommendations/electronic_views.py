from django.http.response import JsonResponse
import discogs_client

discogs_api = discogs_client.Client('my_user_agent/1.0', user_token='iveLOjvMtgyHUUCuyAzElYGLTuWzBeyiOhpjAEYA')


def index(request):
    results = discogs_api.search('Sell', genre='Electronic', format='Vinyl',
                                 currency='GBP', price='10to15', year='2019')
    all_dicts = []
    print(len(results))
    for result in results:
        dict1 = {}
        dict1['title'] = result.title
        all_dicts.append(dict1)
    return JsonResponse(all_dicts, json_dumps_params={'indent': 2}, safe=False)