import websocket

# A websockt Emitter
class WSEmitter():
	def __init__(self, host, port, path):
		self.ws = websocket.create_connection('ws://' + host + ':' + str(port) + path)

	# Celery task?
	def send(self, jsonstr):
		return self.ws.send(jsonstr)

	def close(self):
		return self.ws.close()