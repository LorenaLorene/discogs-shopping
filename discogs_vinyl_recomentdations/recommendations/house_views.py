from django.http.response import JsonResponse
import discogs_client
from django.template import loader

discogs_api = discogs_client.Client('my_user_agent/1.0', user_token='iveLOjvMtgyHUUCuyAzElYGLTuWzBeyiOhpjAEYA')


def index(request):
    results = discogs_api.search('Sell', style='House', format='Vinyl',
                                 currency='GBP', price='5to10')
    all_dicts = []
    print(len(results))
    for result in results:
        dict1 = {}
        dict1['title'] = result.title
        all_dicts.append(dict1)
    return JsonResponse(all_dicts, json_dumps_params={'indent': 2}, safe=False)

    # context = {'list_of_results': }
    # return HttpResponse(template.render(context, request))
