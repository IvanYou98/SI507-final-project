from urllib import response
from flask import Flask, request
import requests

app = Flask(__name__)

GOOGLE_MAP_API_HOST = 'https://maps.googleapis.com/maps/api'
GOOGLE_MAP_API_KEY = 'AIzaSyAQLaMnGgurPe4mLYnr0bNx-8UbxeM9UvM'

YELP_API_KEY = 'KRP7C8GMgshZobRbF4_7Jm3SgZQXUdFDG5O7vz30-dAKyIzVjvHDsGNBPSyxNLgnU70p_iAxB-mO0V417AjEm9DoD-bmxTi_PYT6Yv-drAVCqq7zIQ_1EjM93OlBY3Yx'
YELP_API_HOST = 'https://api.yelp.com'
YELP_SEARCH_PATH = '/v3/businesses/search'
YELP_BUSINESS_PATH = '/v3/businesses/'

DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'Ann Arbor, MI'
SEARCH_LIMIT = 3


@app.route('/')
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


@app.route('/restaurants')
def searchRestaurants():
    url_params = {
        'term': request.args.get('term'),
        'location': request.args.get('location')
    }
    response = requests.request('GET', YELP_API_HOST + YELP_SEARCH_PATH, headers={
        'Authorization': 'Bearer %s' % YELP_API_KEY,
    },  params=url_params)
    return response.json()

# transform geolocation to address


@app.route('/location/current')
def getCurrentLocation():
    url_parameter = {
        'latlng': request.args.get('lat') + ',' + request.args.get('long'),
        'key': GOOGLE_MAP_API_KEY
    }
    response = requests.request(
        'GET', GOOGLE_MAP_API_HOST + '/geocode/json', params=url_parameter)
    return response.json()


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
