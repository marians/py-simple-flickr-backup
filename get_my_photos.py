import flickrapi
import simplejson as json
import xml.etree.ElementTree
import urllib

# Configuration

api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
api_secret = 'xxxxxxxxxxxxxxxx'
user_id = 'xxxxxxxx@N00'

# Configuration end

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='etree')

(token, frob) = flickr.get_token_part_one(perms='write')
if not token: raw_input("Press ENTER after you authorized this program")
flickr.get_token_part_two((token, frob))

for photo in flickr.walk(user_id, per_page=100):
	info = flickr.photos_getInfo(photo_id=photo.get('id'))
	p = info.find('photo')
	url = 'http://farm' + p.get('farm') + '.static.flickr.com/' + p.get('server') + '/' + p.get('id') + '_' + p.get('originalsecret') + '_o.' + p.get('originalformat')
	localfile = p.get('id') + '.' + p.get('originalformat')
	print url
	urllib.urlretrieve(url, localfile)
	
