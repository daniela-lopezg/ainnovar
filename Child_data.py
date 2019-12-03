class Child_data:
	def __init__(self,id,name, parent, child_province, child_age):
		self.userid = id
		self.fullname = name
		self.parentname = parent
		self.province = child_province
		self.age = child_age
		self.bullied_score = 0.0
		self.bully_score = 0.0
		self.interactions_total = 0.0
		self.interactions_bullied = 0.0
		self.interactions_bully = 0.0
		self.impact_level = 0
		self.average_bullying = 0.0

	def set_bully_score(self):
		if(self.interactions_total == 0.0):
			return 0.0
		self.bully_score = self.interactions_bully/self.interactions_total

	def set_bullied_score(self):
		if(self.interactions_total == 0.0):
			return 0.0
		self.bullied_score = self.interactions_bullied/self.interactions_total

	def increase_interactions_bully(self):
		self.interactions_bully = self.interactions_bully + 1.0

	def increase_interactions_bullied(self):
		self.interactions_bullied = self.interactions_bullied + 1.0

	def increase_interactions_total(self):
		self.interactions_total = self.interactions_total + 1.0

	def increase_average_bullying(self, score):
		self.average_bullying = self.average_bullying + score

	def setAverage_bullying(self):
		if(self.interactions_total == 0.0):
			return 0.0
		self.average_bullying = self.average_bullying/self.interactions_total

	def setImpact_level(self, impact):
		self.impact_level = impact

	def getFullname(self):
		return self.fullname

	def getUserid(self):
		return self.userid

	def getBullied_Score(self):
		return self.bullied_score

	def getBully_Score(self):
		return self.bully_score

	def getInteractions_total(self):
		return self.interactions_total

	def getProvince(self):
		return self.province

	def getAverage_bullying(self):
		return self.average_bullying

	
	def getImpact_level(self):
		return self.impact_level
