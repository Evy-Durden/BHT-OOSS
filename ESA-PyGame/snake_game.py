import pygame
import sys
import time
import random


# define colors - rgb
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 100)
green = pygame.Color(0, 255, 100)
blue = pygame.Color(0, 0, 255)

# define the window size
window_size_x = 720
window_size_y = 480

# playing screen
grid_start_x = 0
grid_start_y = 50
grid_end_x = window_size_x
grid_end_y = window_size_y


# intialize pygame -> intializes all the modules contained within pygame
pygame.init()

# game window set up
# create graphical window (width, height), screen is a Surface object
screen = pygame.display.set_mode((window_size_x, window_size_y))
pygame.display.set_caption('ESA2 Snake Game')

# FPF frames per second controller
fps_controller = pygame.time.Clock()

running = True

# game variables
# snake position - array of two values needed for the rect object to draw the snake onto the surface (left, top)
snake_pos = [100, 50]

# snake body intial size
snake_body = [[100,50], [90, 50], [80, 50]]

# prey the snake eats
# using random.randrange to determine the new position of the prey
prey_pos = [random.randrange(1, (window_size_x//10)) * 10, random.randrange(1, (window_size_y//10)) * 10]
prey_spawn = True

# direction of the snake
direction = 'RIGHT'
change_drktn = direction

# intialize score
score = 0


"""
display the current score

"""
def show_score():
    global score
    # create font object
    score_font = pygame.font.SysFont('comic sans', 25)
    # render font object on surface
    score_surface = score_font.render(f'Score: {score}', True, white)
    score_rect = score_surface.get_rect(topleft =(10, 10))

    screen.blit(score_surface, score_rect)



"""
calculate new position of prey

"""
def calc_prey_pos():
    pass

"""
game over function

"""
def game_over():
    pass

"""
populate screen

"""
def render_game():
    pass

"""
main function for executing the game loop

"""
def main():

    global running, fps_controller

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        show_score()

        pygame.display.flip()

        fps_controller.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()