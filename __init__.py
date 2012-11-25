from urlparse import urlparse
from emitter_udp import UDPEmitter
from emitter_ws import WSEmitter
import json
from datetime import datetime


# Emitter factory
# Usage: em = Cube.Emitter('udp://example.com:1080/')
#        em.send({'hello': 'world'})
#		 em.close()

class Emitter:
	def __init__(self, cs):
		o = urlparse(cs)
		
		if o.scheme == 'udp':
			self.sub = UDPEmitter(o.hostname, o.port)

		if o.scheme == 'ws':
			self.sub = WSEmitter(o.hostname, o.port, o.path)

		# TODO: http
	
	# Very simple interface,
	def send(self, obj):
		obj['time'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
		return self.sub.send(json.dumps(obj))

	def close(self):
		return self.sub.close()