from flask_googlemaps import Map


def get_map(bars):
	mymap = Map(
		identifier='view-side',
		lat=bars[0]['lat'],
		lng=bars[0]['long'],
		zoom=12,
		markers=[
			{
				'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
				'lat': bars[i]['lat'],
				'lng': bars[i]['long'],
				'infobox': bars[i]['name']

			} for i in [0,1,2]
		]
	)

	return mymap