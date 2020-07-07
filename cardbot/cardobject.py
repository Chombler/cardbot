

class cardObject(object):
	record = []
	name = ""
	cardclass = []
	tribes = []
	cardType = ""
	cost = 0
	costType = ""
	strength = 0
	strengthModifier = "Strength"
	health = 0
	healthModifier = "Health"
	traits = []
	ability = ""
	flavor = ""
	cardSet = ""
	rarity = ""


	def __init__(self, record):
		self.resetCard()
		self.record = record

		for row in record:
			self.createName(row[0])
			self.createClasses(row[1])
			self.createTribes(row[2])
			self.createType(row[3])
			self.createCost(row[4])
			self.createCostType(row[5])
			self.createStrength(row[6])
			self.createStrengthModifier(row[7])
			self.createHealth(row[8])
			self.createHealthModifier(row[9])
			self.createTraits(row[10])
			self.createAbility(row[11])
			self.createFlavor(row[12])
			self.createCardSet(row[13])
			self.createRarity(row[14])

	def resetCard(self):
		self.record = []
		self.name = ""
		self.cardclass = []
		self.tribes = []
		self.cardType = ""
		self.cost = 0
		self.costType = ""
		self.strength = 0
		self.strengthModifier = "Strength"
		self.health = 0
		self.healthModifier = "Health"
		self.traits = []
		self.ability = ""
		self.flavor = ""
		self.cardSet = ""
		self.rarity = ""


	def createName(self, recordName):
		self.name = recordName
	
	def createClasses(self, recordClass):
		if(recordClass in self.cardclass):
			return
		else:
			self.cardclass.append(recordClass)

	def createTribes(self, recordTribe):
		if(recordTribe is None):
			return
		if(recordTribe in self.tribes):
			return
		else:
			self.tribes.append(recordTribe)

	def createType(self, recordType):
		self.cardType = recordType

	def createCost(self, costRecord):
		self.cost = costRecord
	
	def createCostType(self, recordCostType):
		if(len(self.costType) < 1):
			self.costType = recordCostType
			return
		elif(self.costType == recordCostType):
			return
		else:
			self.costType = "Special"

	def createStrength(self, recordStrength):
		self.strength = recordStrength
	
	def createStrengthModifier(self, recordStrengthModifier):
		if(recordStrengthModifier is None):
			return
		self.strengthModifier = recordStrengthModifier if self.strengthModifier == "Strength" else "Special"

	
	def createHealth(self, recordHealth):
		self.health = recordHealth if self.health != recordHealth else self.health
	
	def createHealthModifier(self, recordHealthModifier):
		if(recordHealthModifier is None):
			return
		self.healthModifier = recordHealthModifier if self.healthModifier == "Health" else "Special"
		
	def createTraits(self, recordTrait):
		if(recordTrait is None):
			return
		if(recordTrait in self.traits):
			return
		else:
			self.traits.append(recordTrait)
	
	def createAbility(self, recordAbility):
		self.ability = recordAbility

	def createFlavor(self, recordFlavor):
		self.flavor = recordFlavor
	
	def createCardSet(self, recordCardSet):
		if(recordCardSet is None):
			return
		self.cardSet = recordCardSet
	
	def createRarity(self, recordRarity):
		self.rarity = recordRarity
	
	def getName(self):
		return(self.name)

	def getClasses(self):
		returnString = ""
		for c in self.cardclass:
			returnString += ":" + c + ":"
		return(returnString)

	def getTribes(self):
		returnString = ""
		for tribe in self.tribes:
			returnString += tribe + " "
		return(returnString)

	def getType(self):
		return(self.cardType)

	def getCost(self):
		return(self.cost)

	def getCostType(self):
		return(self.CostType)

	def getStrength(self):
		return(self.strength)

	def getStrengthModifier(self):
		return(self.strengthModifier)

	def getHealth(self):
		return(self.health)

	def getHealthModifier(self):
		return(self.healthModifier)

	def getStats(self):
		if(self.health != 0):
			if(self.strength != 0):
				return("%s:%s: %s:%s:/%s:%s:" % (self.cost, self.costType, self.strength, self.strengthModifier, self.health, self.healthModifier))
			else:
				return("%s:%s: %s:%s:" % (self.cost, self.costType, self.health, self.healthModifier))
		else:
			return("%s:%s:" % (self.cost, self.costType))

	def getTraits(self):
		returnString = ""
		for trait in self.traits:
			returnString += trait + ", "
		else:
			returnString = returnString[0:-2]
		returnString += "\n" if len(returnString) > 0 else ""
		return(returnString)

	def getAbility(self):
		returnString = self.ability + "\n" if len(self.ability) > 0 else ""
		return(returnString)

	def getFlavor(self):
		return(self.flavor)

	def getSet(self):
		return(self.cardSet + " ")

	def getRarity(self):
		return(self.rarity)

	def information(self):
		return( self.getName() + "\n" +
				self.getClasses() + "\n" +
				self.getTribes() + self.getType() + "\n" +
				self.getStats() + "\n" +
				self.getTraits() +
				self.getAbility() + 
				"*" + self.getFlavor() + "*\n" +
				self.getSet() + "-- " + self.getRarity() + " --")



	def __str__(self):
		return self.name


"""
0name, 
1cardclass.cardclass,
2tribe.tribe, 3cardtype.cardtype,
4cost, 5side.side, 6strength, 7trait.strengthmodifier, 8health, 9trait.healthmodifier,
10trait.trait,
11ability,
12flavor,
13cardset.cardset,
14rarity.rarity
"""
