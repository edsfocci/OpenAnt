
class StatesAnt:
	Idle,MoveAround,GoOutside,FollowTrail,GrabFood,DropFood,Attack,Follow,Exchangefood = range(5)
class AI:

	def __init__(self,ant):
		self.currentAction = StatesAnt.Idle
		self.nextAction = StatesAnt.Idle
		self.lastMovementVector = Coord((0,0,0))
		self.ant = ant
		self.surroundingTilesWeight = zeros(0,8)
		self.trail = Scents.Empty
		slef.currentState = StatesAnt.Idle
		pass
		
class AntAI(AI):
	def __init__(self):
		pass

    def takeDecision(self):
		if currentState = StatesAnt.Idle
			performStateIdle()
		elif currentState = StatesAnt.GoOutside:
			performStateGoOutside()
			
		if self.nextAction = AIActions.Idle
		self.evaluateSurroundings()
		
	def performStateIdle(self):
		pass
		
	def performStateGoOutside(self):
		#get closest exit
		closestExit = self.map.exits[0]
		distance = self.map.getMovementCostTo(closestExit.inside)
		for exit in self.map.exits
			newDistance = self.map.getMovementCostTo(exit.inside) 
			if newDistance < distance:
				distance = newDistance
				closestExit = exit
		self.ant.setAction(closestExit.inside,Actions.Move)		
		
		
	def evaluateTransitions(state):
		if state == StatesAnt.Idle:
			if self.map is Underground:
				state = StatesAnt.GoOutside
		
		if state == StatesAnt.GoOutside:
			if self.map is Outside:
				if self.trailAround():
					state = StatesAnt.FollowTrail
				else:
					state = StatesAnt.MoveAround
	def evaluateSurroundings(self):
		__tiles = self.ant.map.getSurroundings(self.ant.getPos())	#returns a 3x3 tiles[] block
			for tile in __tile:
				if tile.containScent(Scents.Alarm):
					if self.currentAction == AIActions.FollowTrail:
				
					