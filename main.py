#!/usr/bin/python

import pygame
from food import Food

def main():

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
    color1 = (254, 0, 0)
    color2 = (255, 0 ,0)
    player_color = []

    #food
    food = Food()
    def move_player(x, y):
        if len(player) > player_length-1:
            player.pop()
        player.insert(0, (x, y))

        if len(player_color) <= 10: #you can't lose if you collide with first 10 lines
            player_color.insert(-1, color1)
        else:
            player_color.insert(-1, color2)

        if len(player) <= player_length-1: #makes the snake wider in the center
            player_width.insert(int(len(player_width)/2), int(len(player)/(player_length/5)+1))

    #game loop
    loop = True
    alive = True
    groath_rate = 3
    count = 0
    while loop:
        window.fill((0, 0, 0))
        count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEMOTION and alive:
                x, y = event.pos
                if x-food.x >=0 and y-food.y >=0 and x-food.x <=10 and y-food.y <=10:
                    print('{0}, {1}, {2}, {3}'.format(x, y, food.x, food.y))
                    food.eaten()
                    player_length += groath_rate

        food.draw(window)
        try:
            if count == 6 and alive:
                count = 0
                move_player(x, y)

            coordinates_prev = (x, y)
            head = True
            for coordinates, width, color in zip(player, player_width, player_color):
                pygame.draw.line(window, color, coordinates_prev, coordinates, width)
                coordinates_prev = coordinates

            if window.get_at((x, y))[:3] == color2:
                alive = False

        except Exception:
            pass

        clock.tick(60)

        #print(clock.get_fps())
        pygame.display.update()


if __name__ == '__main__':
    main()
