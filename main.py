#!/usr/bin/python3.9

import pygame
import random

class Food:
    def __init__(self):
        self.x = random.randint(0, 790)
        self.y = random.randint(0, 590)
        self.color = (255, 255, 255)
        self.size = 10
    def eaten(self):
        self.x = random.randint(0, 790)
        self.y = random.randint(0, 590)
    def draw(self):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.size, self.size))

if __name__ == '__main__':

    #initialize pygame
    pygame.init()

    #create a window
    window = pygame.display.set_mode((800, 600))

    #pygame clock
    clock = pygame.time.Clock()

    #player
    player = []
    player_length = 10
    player_width = []

    #food
    food = Food()
    def move_player(x, y):
        if len(player) > player_length-1:
            player.pop()
        player.insert(0, (x, y))
        if len(player) <= player_length-1:
            player_width.insert(int(len(player_width)/2), int(len(player)/(player_length/5)+1))
        #print(player)

    #game loop
    loop = True
    #count = 0
    while loop:
        window.fill((0, 0, 0))
        #count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
        if x-food.x >=0 and y-food.y >=0 and x-food.x <=10 and y-food.y <=10:
            print('{0}, {1}, {2}, {3}'.format(x, y, food.x, food.y))
            food.eaten()
            player_length += 3
        food.draw()
                #print("{0} {1}".format(x, y))
        #if count == 4:
            #count = 0
        try:
            move_player(x, y)
            coordinates_prev = (x, y)
            for coordinates, width in zip(player, player_width):
                pygame.draw.line(window, (255, 0, 0), coordinates_prev, coordinates, width)
                coordinates_prev = coordinates
        except Exception:
            pass
        clock.tick(60)
        #print(clock.get_fps())
        #print(player_length)
        pygame.display.update()

