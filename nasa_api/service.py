import os
import requests
import urllib.request

from dotenv import load_dotenv

dotenv_file_path = os.path.join(os.path.dirname(__file__), '../.env')

if dotenv_file_path:
    load_dotenv(dotenv_file_path)


class NasaImageOfTheDay:
    # nasa_api_requests_per_hour_limit = response.headers['X-RateLimit-Limit']
    # nasa_api_requests_remaining = response.headers['X-RateLimit-Remaining']

    def __init__(self):
        self.token = os.getenv('NASA_TOKEN')
        self.nasa_base_url = os.getenv('NASA_URL')

    @staticmethod
    def get_response(link):
        return requests.get(link)

    def get_image_of_the_day_url(self):
        photo_of_the_day_link = self.nasa_base_url + 'planetary/apod?api_key=' + self.token
        response = NasaImageOfTheDay.get_response(photo_of_the_day_link)
        photo_of_the_day_url = response.json().get('url')
        return photo_of_the_day_url

    def write_photo(self):
        with open('media/nasa_photo_of_the_day.jpeg', 'wb'):
            photo_of_the_day = self.get_image_of_the_day_url()
            img = urllib.request.urlopen(photo_of_the_day).read()
            out = open('media/nasa_photo_of_the_day.jpeg', 'wb')
            out.write(img)
