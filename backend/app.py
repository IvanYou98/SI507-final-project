"""
This is the backend server for retrieving data from Yelp Fusion and Google Map API
"""
from flask import Flask, request
import requests
from cache_utils import *
from heap_sort import sort

app = Flask(__name__)

# url and api key for google map api
GOOGLE_MAP_API_HOST = 'https://maps.googleapis.com/maps/api'
GOOGLE_MAP_API_KEY = 'AIzaSyAQLaMnGgurPe4mLYnr0bNx-8UbxeM9UvM'

# url and api key for yelp fusion api
YELP_API_KEY = 'KRP7C8GMgshZobRbF4_7Jm3SgZQXUdFDG5O7vz30-dAKyIzVjvHDsGNBPSyxNLgnU70p_iAxB-mO0V417AjEm9DoD-bmxTi_PYT6Yv-drAVCqq7zIQ_1EjM93OlBY3Yx'
YELP_API_HOST = 'https://api.yelp.com'
YELP_SEARCH_PATH = '/v3/businesses/search'
YELP_BUSINESS_PATH = '/v3/businesses/'

DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'Ann Arbor, MI'
SEARCH_LIMIT = 3


# this is just a testing end point
@app.route('/default')
def hello_world():
    url_params = {
        'term': DEFAULT_TERM.replace(' ', '+'),
        'location': DEFAULT_LOCATION.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    response = requests.request('GET', YELP_API_HOST + YELP_SEARCH_PATH, headers={
        'Authorization': 'Bearer %s' % YELP_API_KEY,
    }, params=url_params)
    return response.json()


"""
Handling the GET request of "/restaurants" end point
"""


@app.route('/restaurants')
def searchRestaurants():
    term = request.args.get('term')
    location = request.args.get('location')

    filename = term + "@" + location + ".json"
    # if we haven't seen this query before, we will open a cache for this request
    cache_data = open_cache(filename)
    if len(cache_data) == 0:
        url_params = {
            'term': term,
            'location': location
        }
        # concatenate url with two path parameters
        response = requests.request('GET', YELP_API_HOST + YELP_SEARCH_PATH, headers={
            'Authorization': 'Bearer %s' % YELP_API_KEY,
        }, params=url_params)
        data = response.json()
        sort(data['businesses'])
        # save to cache for future use
        save_to_cache(data, filename)
        return data
    # if we have seen this query before, we will just return the cached data
    else:
        return cache_data


"""
    transform the latitude and longitude to geocode
"""


@app.route('/location/current')
def getCurrentLocation():
    url_parameter = {
        'latlng': request.args.get('lat') + ',' + request.args.get('long'),
        'key': GOOGLE_MAP_API_KEY
    }
    response = requests.request(
        'GET', GOOGLE_MAP_API_HOST + '/geocode/json', params=url_parameter)
    return response.json()


"""
    transform a location string to geocode
"""


@app.route('/location/geolocation')
def getGeoLocation():
    url_parameter = {
        'address': request.args.get('address'),
        'key': GOOGLE_MAP_API_KEY
    }

    response = requests.request(
        'GET', GOOGLE_MAP_API_HOST + '/geocode/json', params=url_parameter)
    return response.json()


if __name__ == '__main__':
    app.run()
