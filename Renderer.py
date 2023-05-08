import pygame


class Renderer:

	def __init__(self):
		self.setupPygame()

	def setupPygame(self):
		pygame.init()
		self.window = pygame.display.set_mode((600, 600))
		pygame.display.set_caption("Predator vs Prey")

	def render(self, entities):
		self.window.fill((255, 255, 255))
		for entity in entities:
			entity.render(self.window)
		pygame.display.update()
