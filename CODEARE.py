#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import numpy as np
from pygame.locals import *

# Simulation parameters
N = 150
width, height = 500, 500
speed = 20
wiggle = 0.1
collision_radius = 20
alignment_radius = 50
attraction_radius = 100
blind_spot = 120
predator_radius = 0
eating_distance = 5
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

eaten_count = 0
class Agent:
    def __init__(self, position, heading):
        self.position = position
        self.heading = heading

    def update(self, neighbors, predator):
        # Repulsion
        repulsion = np.zeros(2)
        for other in neighbors:
            if np.linalg.norm(self.position - other.position) < collision_radius:
                repulsion += (self.position - other.position)

        # Alignment
        alignment = np.zeros(2)
        count = 0
        for other in neighbors:
            if np.linalg.norm(self.position - other.position) < alignment_radius:
                angle = np.arccos(np.dot(self.heading, other.heading) / (np.linalg.norm(self.heading) * np.linalg.norm(other.heading)))
                if angle < np.radians(blind_spot):
                    alignment += other.heading
                    count += 1
        if count > 0:
            alignment /= count

        # Attraction
        attraction = np.zeros(2)
        count = 0
        for other in neighbors:
            if np.linalg.norm(self.position - other.position) < attraction_radius:
                attraction += other.position
                count += 1
        if count > 0:
            attraction /= count
            attraction -= self.position

        # Predator
        predator_avoidance = np.zeros(2)
        if np.linalg.norm(self.position - predator.position) < predator_radius:
            predator_avoidance += (self.position - predator.position)
            predator_avoidance *= 2
        self.heading += repulsion + alignment + attraction + predator_avoidance
        random_wiggle = np.random.uniform(-wiggle, wiggle, 2)
        self.heading += random_wiggle
        self.heading /= np.linalg.norm(self.heading)
        self.position += speed * self.heading
        self.check_boundaries()

    def check_boundaries(self):
        if self.position[0] < 0:
            self.position[0] = 0
            self.heading[0] = -self.heading[0]
        elif self.position[0] > width:
            self.position[0] = width
            self.heading[0] = -self.heading[0]

        if self.position[1] < 0:
            self.position[1] = 0
            self.heading[1] = -self.heading[1]
        elif self.position[1] > height:
            self.position[1] = height
            self.heading[1] = -self.heading[1]
    
def display_eaten_count():
    global eaten_count
    font = pygame.font.Font(None, 25)
    text = font.render(f'Eaten agents: {eaten_count}', True, (0, 0, 0))
    screen.blit(text, (10, 10))

agents = [Agent(np.random.rand(2) * np.array([width, height]), np.random.rand(2) - 0.5) for _ in range(N)]
predator = Agent(np.random.rand(2) * np.array([width, height]), np.random.rand(2) - 0.5)

running = True
while running:
    screen.fill((255, 255, 255))

    for agent in agents[:]:
        agent.update(agents, predator)
        pygame.draw.circle(screen, (0, 0, 255), agent.position.astype(int), 2)

        # Check if the predator is close enough to eat the agent
        if np.linalg.norm(agent.position - predator.position) < eating_distance:
            agents.remove(agent)
            eaten_count += 1  # Increment the eaten count

    predator.position += speed * predator.heading
    if predator.position[0] < 0:
        predator.position[0] = 0
        predator.heading[0] = -predator.heading[0]
    elif predator.position[0] > width:
        predator.position[0] = width
        predator.heading[0] = -predator.heading[0]

    if predator.position[1] < 0:
        predator.position[1] = 0
        predator.heading[1] = -predator.heading[1]
    elif predator.position[1] > height:
        predator.position[1] = height
        predator.heading[1] = -predator.heading[1]

    pygame.draw.circle(screen, (255, 0, 0), predator.position.astype(int), 5)

    display_eaten_count()
    pygame.display.flip()
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.KEYUP:
            pass

pygame.quit()


# In[ ]:




