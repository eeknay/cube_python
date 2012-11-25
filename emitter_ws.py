

# A websockt Emitter
class WSEmitter():
	def __init__(self, host, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.addr = (host, port)

	# Celery task?
	def send(self, jsonstr):
		print jsonstr
		return self.sock.sendto(jsonstr, self.addr)

	def close(self):
		return self.sock.close()