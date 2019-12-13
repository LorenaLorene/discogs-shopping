from django.http.response import JsonResponse
import discogs_client
import json
import pandas as pd

discogs_api = discogs_client.Client('my_user_agent/1.0', user_token='iveLOjvMtgyHUUCuyAzElYGLTuWzBeyiOhpjAEYA')


def index(request):
    results = discogs_api.search('Sell', genre='Blues', format='Vinyl',
                                 currency='GBP', price='5to10')

    # results2 = discogs_api.artist(id='322292')

    all_dicts = []
    for result in results:
        dict1 = {}
        dict1['title'] = result.title
        all_dicts.append(dict1)
        # all_dicts = pd.array()
    return JsonResponse(all_dicts, json_dumps_params={'indent': 2}, safe=False)
    # return all_dicts


# a = pd.read_json()
# print(a)
