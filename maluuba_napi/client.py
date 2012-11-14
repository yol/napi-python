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

	class InterpretResponse(object):
		def __init__(self, action, category, entities={}):
			self.action = action
			self.category = category
			self.entities = entities

	class NormalizeResponse(object):
		def __init__(self, entities={}, context={}):
			self.entities = entities
			self.context = context

	def __init__(self, api_key):
		self.api_key = api_key

	def __query(self, endpoint, **kwargs):
		kwargs['apikey'] = self.api_key
		r = requests.get(self.__generate_url(endpoint), params=kwargs)
		print 'Called %s' % r.url
		if r.status_code == 200:
			try:
				return json.loads(r.content)
			except Exception as e:
				print "Failed to parse response: %s" % r.content
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
		return NAPIClient.InterpretResponse(**(self.__query('interpret', phrase=phrase)))

	def normalize(self, phrase, _type, timezone=''):
		"""
		Normalizes a time, date, or range.
		"""
		return NAPIClient.NormalizeResponse(**(self.__query('normalize', phrase=phrase, type=_type, timezone=timezone)))