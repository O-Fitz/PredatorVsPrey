import numpy as np
import pygame
import math
from Entity import Entity
from Renderer import Renderer
from Simulation import Simulation


def main():
    vec1 = np.array([100.0, 200.0])
    vec2 = np.array([0.0, 0.0])
    vec3 = vec1 + vec2
    print(vec3.tolist())

    #entities = [Entity(vec1, vec2, 0, math.pi/2, (255, 0, 0), (0, 255, 0), 10)]
    renderer = Renderer()
    simulation = Simulation()
    play = True

    timer = pygame.time.Clock()
    fpsCap = 120

    substeps = 5

    while play:
        timer.tick(fpsCap)
        dt = float(timer.get_time()/1000)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                play = False

        for i in range(substeps):
            simulation.update(dt/substeps)

        renderer.render(simulation.get_entities())


if __name__ == '__main__':
    main()

