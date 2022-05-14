import pygame
import random

pygame.font.init()

s_width = 800
s_height = 700

play_width = 300
play_height = 600

block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = (s_height -play_height)


J = [[False,True,False],[False,True,False],[True,True,False]]
L = [[False,True,False],[False,True,False],[False,True,True]]
I = [[False,False,False,False],[True,True,True,True],[False,False,False,False],[False,False,False,False]]
T = [[False,False,False],[False,True,False],[True,True,True]]
O = [[True,True],[True,True]]
S = [[False,False,False],[False,True,True],[True,True,False]]
Z = [[False,False,False],[True,True,False],[False,True,True]]



shapes = [S,Z,I,O,J,L,T]
shape_color = [(220,20,60),(0,255,0),(0,255,255),(255,255,0),(255,20,147),(255,140,0),(138,43,226),]


class Piece(object):
    def __init__(self,shape):
        self.shape = shape
        self.color = shape_color[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_position={}):
    grid = [[0 for column in range(10)] for row in range(20)]
    return grid
def convert_shape_format(shape):
    pass

def valid_shape(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    shape = Piece(random.choice(shapes))
    print(shape.shape)
    print(shape.color)

def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont("player 1",size, bold=True)
    label = font.render(text, 1 , (255,255,255))
    surface.blit(label,(top_left_x+play_width/2 - (label.get_width()/2),
                        top_left_y+play_height/2 - (label.get_height()/2)))

def draw_grid(surface, row, col):
    pass

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont("player 1", 30, bold=True)
    label = font.render("Next Piece", 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width / 0.8 - (label.get_width() / 20),300))



def draw_window(win,grid):
    win.fill((0,0,0))
    font = pygame.font.SysFont("player 1", 60, bold=True)
    label = font.render("Tetris", 1, (255, 255, 255))
    win.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2),30))
    pygame.draw.rect(win,(255,0,0),(top_left_x,top_left_y,play_width,play_height),5)
def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            if event.type == pygame.K_UP:
                print("HEY YOU PRESSED UP BUTTON")
                current_piece.rotation += 1
                print(current_piece.rotation)
        draw_window(win,grid)
        draw_next_shape(next_piece, window)
        pygame.display.update()


def main_menu(win):
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle("Press any key to play",60,(255,255,255),win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
            if event.type == pygame.KEYDOWN:
                main(win)
    pygame.display.quit()

window = pygame.display.set_mode((s_width,s_height))
main_menu(window)