from serpapi import GoogleSearch
import json
from PIL import Image, ImageTk
import requests
from io import BytesIO


class ImageDownloader:

    def __init__(self, q):
        self.q = q
        self.params = {
            "engine": "google",
            "ijn": "0",
            "q": q,
            "google_domain": "google.com",
            "tbm": "isch",
            "api_key": "f54e2cc2fe41534191097606ee44a815035d74f3790d7500fe880d4ea6f00444"
        }

    def search_link(self):
        search = GoogleSearch(self.params)
        results = search.get_dict()
        return results["images_results"][0]["original"]

    @staticmethod
    def download_image(url, item_name):
        response = requests.get(url)
        im = Image.open(BytesIO(response.content))
        im = im.resize((100, 75), Image.ANTIALIAS)
        im.save("./img/" + item_name + ".jpg")
        img = ImageTk.PhotoImage(im)
        return img


# imd = ImageDownloader()
# res = imd.search()["images_results"][0]["original"]
# print(res)
