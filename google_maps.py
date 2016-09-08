from flask_googlemaps import Map


def get_map(bars):
	mymap = Map(
		identifier='view-side',
		lat=bars[0]['lat'],
		lng=bars[0]['long'],
		markers=[
			{
				'icon': bars[0]['image'],
				'lat': bars[0]['lat'],
				'lng': bars[0]['long'],
				'infobox': bars[0]['name']

			}
		]
	)

	return mymap