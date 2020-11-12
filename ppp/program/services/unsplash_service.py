from django.conf import settings
import requests


class UnsplashService():
    def __init__(self):
        self.key = settings.UNSPLASH_ACCESS_KEY
        self.photo_search_url = settings.UNSPLASH_PHOTO_SEARCH_URL

    def search_query(self, keyword, count=10, quality="regular"):
        params = {'client_id': self.key, "query": keyword, "per_page": count}
        req = requests.get(url=self.photo_search_url, params=params)
        status =req.status_code
        data = req.json()

        res = []

        for item in data['results']:
            img = dict()
            img['url'] = item['urls'][quality]
            img['thumb'] = item['urls']['thumb']
            img['alt'] = item['alt_description']
            res.append(img)

        return res
