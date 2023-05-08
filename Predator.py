from Entity import Entity


class Predator(Entity):

	def __init__(self, position, velocity, angle, angleVel, maxEnergy, radius):
		super().__init__(position, velocity, angle, angleVel, maxEnergy, (255, 0, 0), (0, 0, 255), radius, 1)

	def update(self, dt):
		super().update(dt)

		if self.energy <= 0:
			print(self.position)
			self.should_die = True

	def eat(self, value):
		self.energy = min(self.energy+value, self.maxEnergy)
