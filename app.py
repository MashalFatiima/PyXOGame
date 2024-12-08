import sys
import numpy as np
import pygame

pygame.init()

WINNER = 0
START = (0,0)
END = (0,0)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (180, 180, 180)

WIDTH = 300  
HEIGHT = 300  
BOARD_ROWS = 3  
BOARD_COLS = 3  
SQUARE_SIZE = WIDTH // BOARD_ROWS
LINE_WIDTH = 5   
CIRCLE_RADIUS = SQUARE_SIZE // 3  
CIRCLE_WIDTH = 15  
CROSS_WIDTH = 25  
WINNING_LINE_WIDTH = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Tic-Tac-Toe Game")  
screen.fill(BLACK) 

board = np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_lines(color=WHITE):
    for i in range(1, BOARD_ROWS):
        start_pos_hor = (0, SQUARE_SIZE * i)  
        end_pos_hor = (WIDTH, SQUARE_SIZE * i)  
        pygame.draw.line(screen, color, start_pos_hor, end_pos_hor, LINE_WIDTH)

    for i in range(1, BOARD_COLS):
        start_pos_ver = (SQUARE_SIZE * i, 0) 
        end_pos_ver = (SQUARE_SIZE * i, HEIGHT) 
        pygame.draw.line(screen, color, start_pos_ver, end_pos_ver, LINE_WIDTH)

def draw_figures(color=WHITE):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):

            if board[row][col] == 1: 
                pygame.draw.circle(screen, color, ( int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)

            elif board[row][col] == 2:  
                pygame.draw.line(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE // 4,  row * SQUARE_SIZE + SQUARE_SIZE // 4),    (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), CROSS_WIDTH)
                pygame.draw.line(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4),     CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    global START, END 
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            START = (SQUARE_SIZE * col + SQUARE_SIZE  //2, 0) 
            END   = (SQUARE_SIZE * col + SQUARE_SIZE // 2, HEIGHT) 
            return True
        
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            START = (0, SQUARE_SIZE * row + SQUARE_SIZE  //2) 
            END   = (HEIGHT, SQUARE_SIZE * row + SQUARE_SIZE // 2) 
            return True
        
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        START = (0 * SQUARE_SIZE + SQUARE_SIZE // 4,  0 * SQUARE_SIZE + SQUARE_SIZE // 4)
        END   = (2 * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, 2 * SQUARE_SIZE + 3 * SQUARE_SIZE // 4)
        return True
    
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        START = (2 * SQUARE_SIZE + 3 * SQUARE_SIZE // 4,  0 * SQUARE_SIZE + SQUARE_SIZE // 4)
        END   = (0 * SQUARE_SIZE + SQUARE_SIZE // 4, 2 * SQUARE_SIZE + 3 * SQUARE_SIZE // 4)
        return True
    return False

def win_line():
    pygame.draw.line(screen, WHITE, START, END, WINNING_LINE_WIDTH)

def restart_game():
    screen.fill(BLACK)                        
    draw_lines()                              
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0              

draw_lines()
player = 1  
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:  
            mouseX = event.pos[0] // SQUARE_SIZE  
            mouseY = event.pos[1] // SQUARE_SIZE  
            if available_square(mouseY, mouseX):  
                mark_square(mouseY, mouseX, player)  
                if check_win(player): 
                    game_over = True
                    WINNER = player  
                else:
                    player = player % 2 + 1 
                    if event.type == pygame.MOUSEBUTTONDOWN and not game_over:  
                        mouseX = event.pos[0] // SQUARE_SIZE  
                        mouseY = event.pos[1] // SQUARE_SIZE  
                        if available_square(mouseY, mouseX):  
                            mark_square(mouseY, mouseX, player)  
                            if check_win(player):  
                                game_over = True
                                WINNER = player 
                            else:
                                player = player % 2 + 1  
            if  is_board_full():
               game_over = True
               WINNER = 0
               
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r:
                restart_game()
                game_over = False
                player = 1

    if not game_over:
        draw_figures()
    else:
        if WINNER == 1:  
            draw_figures(GREEN)
            draw_lines(GREEN)
            win_line()
        elif WINNER == 2:
            draw_figures(RED)
            draw_lines(RED)
            win_line()
        else: 
            draw_figures(GRAY)
            draw_lines(GRAY)

    pygame.display.update()