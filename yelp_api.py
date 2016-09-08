from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def find_bars(address):
	auth = Oauth1Authenticator(
	    consumer_key=os.environ['YELP_CONSUMER_KEY'],
	    consumer_secret=os.environ['YELP_CONSUMER_SECRET'],
	    token=os.environ['YELP_TOKEN'],
	    token_secret=os.environ['YELP_TOKEN_SECRET']
	)

	client = Client(auth)

	params = {
	    'term': 'bar',
	    'limit': 3,
	    'sort': 0
	}

	response = client.search(address, **params)

	bars = []
	for business in response.businesses:
	    bars.append({
	    	'name': business.name,
	    	'phone': business.display_phone,
	    	'image': business.image_url,
	    	'rating': business.rating_img_url_small,
	    	'location': business.location.display_address[0],
	    	'lat': business.location.coordinate.latitude,
	    	'long': business.location.coordinate.longitude
	    })

	return bars

