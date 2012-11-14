import json

import requests

class NAPINormalizeType(object):
	"""
	The types of entities that the normalize endpoint can work with.
	"""
	Time, DateRange, TimeRange = ('time', 'daterange', 'timerange')

class NAPIClient(object):
	"""
	A connection to the Maluuba NAPI.
	"""
	BASE_URL = 'http://napi.maluuba.com'
	VERSION  = 'v0'

	def __init__(self, api_key):
		self.api_key = api_key

	def __query(self, endpoint, **kwargs):
		kwargs['apikey'] = self.api_key
		r = requests.get(self.__generate_url(endpoint), params=kwargs)
		print 'Called %s' % r.url
		if r.status_code == 200:
			try:
				return json.loads(r.content)
			except:
				print "Failed to parse JSON: %s" % r.content
				pass
		else:
			print "Failure: %s" % r.status_code

	def __generate_url(self, endpoint):
		return '%s/%s/%s' % (NAPIClient.BASE_URL, NAPIClient.VERSION, endpoint)

	def interpret(self, phrase):
		"""
		The primary endpoint of the NAPI. Classifies the given phrase, and extracts
		entities.
		"""
		return self.__query('interpret', phrase=phrase)

	def normalize(self, phrase, _type, timezone=''):
		"""
		Normalizes a time, date, or range.
		"""
		return self.__query('normalize', phrase=phrase, type=_type, timezone=timezone)