class Province:
	def __init__(self, name):
		self.name = name
		self.interactions = 0.0

	def getName(self):
		return self.name

	def getInteractions(self):
		return self.interactions

	def increaseInteractions(self):
		self.interactions = self.interactions + 1.0
	
