import numpy as np
import math
import pygame

import Maths


class Entity:
	def __init__(self, position, velocity, angle, angleVel, maxEnergy, colour1, colour2, radius, foodChain):
		self.position = position
		self.velocity = velocity
		self.colour1 = colour1
		self.colour2 = colour2
		self.radius = radius
		self.angle = angle
		self.ang_velocity = angleVel
		self.foodChain = foodChain

		self.energy = maxEnergy
		self.maxEnergy = maxEnergy
		self.energyScalar = 0.5

		self.should_die = False

	def render(self, window):
		pygame.draw.circle(window, self.colour1, self.position, self.radius)
		endPos = self.position + np.array([math.cos(self.angle), math.sin(self.angle)])*self.radius
		pygame.draw.line(window, self.colour2, self.position, endPos, 2)

	def update(self, dt):
		self.position += self.velocity * dt
		self.angle += self.ang_velocity * dt

		self.energy -= Maths.mag(self.velocity) * self.energyScalar * dt

	def eat(self, value):
		pass

	def breed(self):
		pass

	def get_position(self):
		return self.position

	def get_radius(self):
		return self.radius

	def get_foodchain(self):
		return self.foodChain

	def die(self):
		return self.should_die
