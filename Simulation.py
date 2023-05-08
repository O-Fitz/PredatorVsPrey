import numpy as np
from Entity import Entity
from Predator import Predator
import Maths


class Simulation:

	def __init__(self):
		self.entities = []
		pos1 = np.array([100.0, 100.0])
		pos2 = np.array([200.0, 200.0])
		#self.entities.append(Entity(pos1, pos1/2, 0, 0, 10, (255, 0, 0), (0, 255, 0), 10, 1))
		self.entities.append(Entity(pos2, np.zeros(2), 0, 0, 10, (0, 0, 255), (0, 255, 0), 10, 0))
		self.entities.append(Predator(pos1, pos1/2, 0, 0, 100, 10))

		self.predatorEatValue = 20

	def update(self, dt):
		dead = []
		# Update entities
		for entity in self.entities:
			entity.update(dt)
			# Check if entities are dead
			if entity.die():
				dead.append(entity)

		# Remove dead entities
		for dead_entity in dead:
			self.entities.remove(dead_entity)

		self.collisionDetection()

	def collisionDetection(self):
		for i, e1 in enumerate(self.entities):
			for j, e2 in enumerate(self.entities):
				# Check that e1 is a predator of e2
				if e1.get_foodchain() > e2.get_foodchain():
					self.checkCollision(i, j)

	def checkCollision(self, i, j):
		# Find the separation of the objects
		sep = self.entities[i].get_position() - self.entities[j].get_position()
		# Find the sum of the radii
		radsum = self.entities[i].get_radius() + self.entities[j].get_radius()
		# If the separation is less than the sum of the radii, they are colliding
		if Maths.mag(sep) < radsum:
			self.handleCollision(i, j)

	def handleCollision(self, i, j):
		self.entities[i].eat(self.predatorEatValue)
		self.entities.pop(j)

	def get_entities(self):
		return self.entities

