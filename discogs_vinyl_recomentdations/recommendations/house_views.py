from django.http.response import JsonResponse
import discogs_client
import numpy as np

discogs_api = discogs_client.Client('my_user_agent/1.0', user_token='iveLOjvMtgyHUUCuyAzElYGLTuWzBeyiOhpjAEYA')


def get_house_recommendations(request):
    results = discogs_api.search('Sell', style='House', format='Vinyl',
                                 currency='GBP', price='5to10', year='2019')

    all_recommendations = []
    # for each search result
    for result in results:
        recommendation = {}
        # we request release by id to get full data
        release = discogs_api.release(result.id)
        recommendation['title'] = release.title
        recommendation['id'] = release.id
        recommendation['artists'] = []
        recommendation['labels'] = []
        # generate own price to add more data as I couldn't retrieve from api
        price = np.random.randint(0, 100) / 10
        recommendation['price'] = price
        for label in release.labels:
            recommendation['labels'].append({
                "id": label.id,
                "name": label.name
            })
        for artist in release.artists:
            recommendation['artists'].append({
                "id": artist.id,
                "name": artist.name
            })
        all_recommendations.append(recommendation)
        sorted_by_price = sorted(all_recommendations, key=lambda i: i['price'])
    return JsonResponse(sorted_by_price, json_dumps_params={'indent': 2}, safe=False)

