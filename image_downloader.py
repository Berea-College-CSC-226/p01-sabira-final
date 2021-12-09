from serpapi import GoogleSearch
import json
from PIL import Image, ImageTk
import requests
from io import BytesIO


class ImageDownloader:
    """
    Helper class to download image from Google
    """

    def __init__(self, q):
        """
        Initializes ImageDownloader class accepting search query as an argument
        :param q: search query string (Apple, Coke and etc.)
        :return: ImageDownloader object
        """
        self.q = q

        # Setting API parameters
        self.params = {
            "engine": "google",
            "ijn": "0",
            "q": q,
            "google_domain": "google.com",
            "tbm": "isch",
            "api_key": "f54e2cc2fe41534191097606ee44a815035d74f3790d7500fe880d4ea6f00444"
        }

    def search_link(self):
        """
        Function to use SerpAPI to get the link
        :return: String
        """

        # Invoke API for Google Image search
        # Returns JSON file with image links
        search = GoogleSearch(self.params)

        # Converts JSON to dictionary
        results = search.get_dict()

        # Extract only first image link
        return results["images_results"][0]["original"]

    @staticmethod
    def download_image(url, item_name):
        """
        Function to download image from link
        :param url: link for image in the Internet
        :param item_name: string name of the item related to the image
        :return: Object
        """

        # Get image byte array from the link
        response = requests.get(url)

        # Read image from byte array
        im = Image.open(BytesIO(response.content))

        # Resize image to constant dimensions
        im = im.resize((100, 75), Image.ANTIALIAS)

        # Save image to file
        im.save("./img/" + item_name + ".jpg")

        # Convert image to format understandable by Tkinter
        img = ImageTk.PhotoImage(im)
        return img

