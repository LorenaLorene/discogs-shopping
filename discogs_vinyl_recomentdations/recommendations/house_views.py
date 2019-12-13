from django.http.response import JsonResponse
import discogs_client

discogs_api = discogs_client.Client('my_user_agent/1.0', user_token='iveLOjvMtgyHUUCuyAzElYGLTuWzBeyiOhpjAEYA')


def get_house_recommendations(request):
    results = discogs_api.search('Sell', style='House', format='Vinyl',
                                 currency='GBP', price='5to10')
    by_label = discogs_api.label(id='98')
    print("by label", by_label)

    by_price = discogs_api.fee_for(price=6.99, currency="GBP")
    print('by_price', by_price)

    all_dicts = []
    print(len(results))
    for result in results:
        dict1 = {}
        dict1['title'] = result.title
        all_dicts.append(dict1)
    return JsonResponse(all_dicts, json_dumps_params={'indent': 2}, safe=False)

