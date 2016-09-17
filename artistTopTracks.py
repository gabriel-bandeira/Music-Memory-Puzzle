#urn = sys.argv[1]
#name = ' '.join(sys.argv[1:])
#print json.dumps(results, indent=4, separators=(',',': '))
#results = spotify.search(q='artist:' + name, type='artist')

import spotipy
import sys
import pprint

import urllib, cStringIO
import Image

def getImages(sp, name):
	if len(name) > 0:
		results = sp.search(q='artist:' + name, type='artist') # error 0
		urn = 'spotify:artist:' + results["artists"]["items"][0]["id"]
	else:
		urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

	response = sp.artist_top_tracks(urn) # error 1
	images = []
	for track in response['tracks']:
		medium_img_link = track["album"]["images"][1]["url"]
		print(track["name"] + ' (image link: ' + str(medium_img_link) + ')')
		file = cStringIO.StringIO(urllib.urlopen(medium_img_link).read()) # error 2
		img = Image.open(file)
		images.append(img)

	return images

def getSamples(sp, name):
	if len(name) > 0:
		results = sp.search(q='artist:' + name, type='artist') # error 0
		urn = 'spotify:artist:' + results["artists"]["items"][0]["id"]
	else:
		urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

	response = sp.artist_top_tracks(urn) # error 1
	samples = []
	for track in response['tracks']:
		#medium_img_link = results["artists"]["items"][i]["images"][1]["url"]
		sample = track["preview_url"]
		print(track["name"] + ' (sample link: ' + str(sample) + ')')
		samples.append(sample)

	return samples


def main():
	sp = spotipy.Spotify()

	if len(sys.argv) > 1:
		name = str(sys.argv[1:])
		results = sp.search(q='artist:' + name, type='artist') # error 0
		urn = 'spotify:artist:' + results["artists"]["items"][0]["id"]
	else:
		urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
	#if len(name) > 0:
	#	results = sp.search(q='artist:' + name, type='artist') # error 0
	#	urn = 'spotify:artist:' + results["artists"]["items"][0]["id"]
	#else:
	#	urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

	response = sp.artist_top_tracks(urn) # error 1
	i=0
	images = []
	for track in response['tracks']:
		#medium_img_link = results["artists"]["items"][i]["images"][1]["url"]
		medium_img_link = track["album"][0]["images"][1]["url"]
		print(track["name"] + ' (image link: ' + str(medium_img_link) + ')')
		file = cStringIO.StringIO(urllib.urlopen(medium_img_link).read()) # error 2
		img = Image.open(file)
		images.append(img)
		i = i+1
		#img.show()
#print json.dumps(response, indent=4, separators=(',',': '))

'''error 0 results:
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "/usr/local/lib/python2.7/dist-packages/spotipy/client.py", line 323, in search
	    return self._get('search', q=q, limit=limit, offset=offset, type=type)
	  File "/usr/local/lib/python2.7/dist-packages/spotipy/client.py", line 133, in _get
	    return self._internal_call('GET', url, payload, kwargs)
	  File "/usr/local/lib/python2.7/dist-packages/spotipy/client.py", line 96, in _internal_call
	    r = self._session.request(method, url, headers=headers, **args)
	  File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 455, in request
	    resp = self.send(prep, **send_kwargs)
	  File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 558, in send
	    r = adapter.send(request, **kwargs)
	  File "/usr/lib/python2.7/dist-packages/requests/adapters.py", line 378, in send
	    raise ConnectionError(e)
	requests.exceptions.ConnectionError: HTTPSConnectionPool(host='api.spotify.com', port=443): Max retries exceeded with url: /v1/search?q=artist%3Ared+hot&type=artist&limit=10&offset=0 (Caused by <class 'socket.gaierror'>: [Errno -2] Name or service not known)
'''

'''error 1 artists top track:
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "/usr/local/lib/python2.7/dist-packages/spotipy/client.py", line 268, in artist_top_tracks
	    return self._get('artists/' + trid + '/top-tracks', country=country)
	  File "/usr/local/lib/python2.7/dist-packages/spotipy/client.py", line 133, in _get
	    return self._internal_call('GET', url, payload, kwargs)
	  File "/usr/local/lib/python2.7/dist-packages/spotipy/client.py", line 96, in _internal_call
	    r = self._session.request(method, url, headers=headers, **args)
	  File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 455, in request
	    resp = self.send(prep, **send_kwargs)
	  File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 558, in send
	    r = adapter.send(request, **kwargs)
	  File "/usr/lib/python2.7/dist-packages/requests/adapters.py", line 378, in send
	    raise ConnectionError(e)
	requests.exceptions.ConnectionError: HTTPSConnectionPool(host='api.spotify.com', port=443): Max retries exceeded with url: /v1/artists/0L8ExT028jH3ddEcZwqJJ5/top-tracks?country=US (Caused by <class 'socket.gaierror'>: [Errno -2] Name or service not known)
'''

'''error 2 url open:
	Traceback (most recent call last):
	  File "<stdin>", line 5, in <module>
	  File "/usr/lib/python2.7/urllib.py", line 87, in urlopen
	    return opener.open(url)
	  File "/usr/lib/python2.7/urllib.py", line 208, in open
	    return getattr(self, name)(url)
	  File "/usr/lib/python2.7/urllib.py", line 437, in open_https
	    h.endheaders(data)
	  File "/usr/lib/python2.7/httplib.py", line 975, in endheaders
	    self._send_output(message_body)
	  File "/usr/lib/python2.7/httplib.py", line 835, in _send_output
	    self.send(msg)
	  File "/usr/lib/python2.7/httplib.py", line 797, in send
	    self.connect()
	  File "/usr/lib/python2.7/httplib.py", line 1178, in connect
	    self.timeout, self.source_address)
	  File "/usr/lib/python2.7/socket.py", line 553, in create_connection
	    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
	IOError: [Errno socket error] [Errno -2] Name or service not known
'''

if __name__ == '__main__':
	if len(sys.argv) > 1:
		name = str(sys.argv[1:])
		getImages(name)
	main()
