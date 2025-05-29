import pygame
import sys
import time
import random

# dictionary for game state

game_state = {'score': 0, 
              'running': True, 
              'snake_pos': [300, 200], 
              'snake_body': [[300,200]],
              'direction': 'RIGHT',
              'change_drctn': 'RIGHT',
              'prey_pos': [100, 100], 
              'prey_spawn': True}



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

# dictionary for gfx

gfx = {'black': black,
       'white': white,
       'red': red,
       'green': green,
       'blue': blue,
       'grid_start_x': grid_start_x,
       'grid_start_y': grid_start_y,
       'grid_end_x': grid_end_x,
       'grid_end_y': grid_end_y,
       'screen': screen,
       'fps_controller': fps_controller}


# functions

"""
display the current score

"""
def show_score():
    global game_state
    # create font object
    score_font = pygame.font.SysFont('comic sans', 25)
    # render font object on surface
    score_surface = score_font.render(f'Score: {game_state['score']}', True, white)
    score_rect = score_surface.get_rect(topleft =(10, 10))

    gfx['screen'].blit(score_surface, score_rect)



"""
handling the snake

"""
def handle_snake():
    global game_state, gfx

    # moving the snake
    if game_state['direction'] == 'UP':
        game_state['snake_pos'][1] -= 10
    if game_state['direction'] == 'DOWN':
        game_state['snake_pos'][1] += 10
    if game_state['direction'] == 'LEFT':
        game_state['snake_pos'][0] -= 10
    if game_state['direction'] == 'RIGHT':
        game_state['snake_pos'][0] += 10

    # growing mechanism of the snake
    game_state['snake_body'].insert(0, list(game_state['snake_pos']))
    if game_state['snake_pos'][0] == game_state['prey_pos'][0] and game_state['snake_pos'][1] == game_state['prey_pos'][1]:
        game_state['score'] += 10
        game_state['prey_spawn'] = False
    else:
        game_state['snake_body'].pop()

    if not game_state['prey_spawn']:
        calc_prey_pos()
        
    game_state['prey_spawn'] = True
    gfx['screen'].fill(gfx['black'])

"""
calculate new position of prey

"""
def calc_prey_pos():

    global game_state, gfx

    game_state['prey_pos'] = [random.randrange(1, (gfx['grid_end_x']//10)) * 10, 
                              random.randrange(gfx['grid_start_y'], (gfx['grid_end_y']))] #(gfx['grid_end_y']//10)) * 10

"""
game over function

"""
def game_over():

    global game_state, gfx

    g_o_font = pygame.font.SysFont('comic sans', 40)
    g_o_surface = g_o_font.render(f'Game Over - You Died! \n Total Score: {game_state['score']}', True, white)
    g_o_rect = g_o_surface.get_rect(midtop= (gfx['grid_end_x']//2, gfx['grid_end_y']//2))

    gfx['screen'].fill(gfx['black'])
    gfx['screen'].blit(g_o_surface, g_o_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()
    

"""
populate screen with drawings

"""
def render_game():
    global game_state, gfx

    gfx['screen'].fill(gfx['black'])

    # render score
    show_score()
    
    # render horizontal line for separating the playing are from the info area
    horizontal_line = pygame.draw.line(gfx['screen'], gfx['red'], (gfx['grid_start_x'], gfx['grid_start_y']), (gfx['grid_end_x'], gfx['grid_start_y']))

    # render snake
    for position in game_state['snake_body']:
        snake_rect = pygame.Rect(position[0], position[1], 10, 10)
        pygame.draw.rect(gfx['screen'], gfx['blue'], snake_rect)
    
    # render prey
    prey_rect = pygame.Rect(game_state['prey_pos'][0], game_state['prey_pos'][1], 10, 10)
    pygame.draw.rect(gfx['screen'], gfx['green'], prey_rect)

    pygame.display.flip()


"""
main function for executing the game loop

"""
def main():

    global game_state, gfx

    # game loop
    while game_state['running']:

        # handling the key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_state['change_drctn'] = 'UP'
                if event.key == pygame.K_DOWN:
                    game_state['change_drctn'] = 'DOWN'
                if event.key == pygame.K_LEFT:
                    game_state['change_drctn'] = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    game_state['change_drctn'] = 'RIGHT'
        
        # in case two keys are pressed simultaneously
        if game_state['change_drctn'] == 'UP' and game_state['direction'] != 'DOWN':
            game_state['direction'] = 'UP'
        if game_state['change_drctn'] == 'DOWN' and game_state['direction'] != 'UP':
            game_state['direction'] = 'DOWN'
        if game_state['change_drctn'] == 'LEFT' and game_state['direction'] != 'RIGHT':
            game_state['direction'] = 'LEFT'
        if game_state['change_drctn'] == 'RIGHT' and game_state['direction'] != 'LEFT':
            game_state['direction'] = 'RIGHT'

        handle_snake()
        
        render_game()


        # game over conditions
        # snake is getting out of bounds
        if game_state['snake_pos'][0] < 0 or game_state['snake_pos'][0] > gfx['grid_end_x']:
            game_over()
        if game_state['snake_pos'][1] < gfx['grid_start_y'] or game_state['snake_pos'][1] > gfx['grid_end_y']:
            game_over()

        # snake bites itself
        for parts in game_state['snake_body'][1:]:
            if game_state['snake_pos'][0] == parts[0] and game_state['snake_pos'][1] == parts[1]:
                game_over()

        pygame.display.update()

        gfx['fps_controller'].tick(10)

    pygame.quit()


if __name__ == '__main__':
    main()