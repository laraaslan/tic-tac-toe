import pygame
import sys

# Oyun tahtasi
board = [[' ' for _ in range(3)] for _ in range(3)]

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ekran boyutu
WIDTH, HEIGHT = 300, 300
SCREEN_SIZE = (WIDTH, HEIGHT)

# Kare boyutu
SQUARE_SIZE = WIDTH // 3

# X ve O resimleri
X_IMAGE = pygame.image.load('x_image.png')
O_IMAGE = pygame.image.load('o_image.png')


# Oyun tahtasi
def draw_board():
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 0)
            if board[row][col] == 'X':
                screen.blit(X_IMAGE, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif board[row][col] == 'O':
                screen.blit(O_IMAGE, (col * SQUARE_SIZE, row * SQUARE_SIZE))


# Oyun tahtasindaki pozisyon
def get_square(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return row, col


# Oyun tahtasini kontrol etme
def check_winner():
    # Rows
    for row in board:
        if all(cell == 'X' for cell in row) or all(cell == 'O' for cell in row):
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)) or \
                all(board[row][col] == 'O' for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return True
    return False


# Oyun baslatma
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

current_player = 'X'

running = True
while running:
    screen.fill(BLACK)
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_player == 'X':
                row, col = get_square(pygame.mouse.get_pos())
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    if check_winner():
                        print("X wins!")
                        running = False
                    else:
                        current_player = 'O'
            else:
                row, col = get_square(pygame.mouse.get_pos())
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    if check_winner():
                        print("O wins!")
                        running = False
                    else:
                        current_player = 'X'

    clock.tick(30)

pygame.quit()
sys.exit()
