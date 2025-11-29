import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("X O Game")
white = (255,255,255)
black = (0,0,0)
board =[["","",""],["","",""],["","",""]]
player = "X"
font = pygame.font.Font(None, 100)

# Add: simple winner check
def check_winner(b):
    lines = []
    # rows and cols
    for i in range(3):
        lines.append(b[i][0] + b[i][1] + b[i][2])
        lines.append(b[0][i] + b[1][i] + b[2][i])
    # diagonals
    lines.append(b[0][0] + b[1][1] + b[2][2])
    lines.append(b[0][2] + b[1][1] + b[2][0])
    if "XXX" in lines:
        return "X"
    if "OOO" in lines:
        return "O"
    # draw?
    if all(b[r][c] != "" for r in range(3) for c in range(3)):
        return "Draw"
    return None

def reset_board():
    for r in range(3):
        for c in range(3):
            board[r][c] = ""
    return "X"

run = True
game_over = False
winner = None

while run:
    screen.fill(white)
    pygame.draw.line(screen,black,(200,0),(200,600),5)
    pygame.draw.line(screen,black,(400,0),(400,600),5)
    pygame.draw.line(screen,black,(0,200),(600,200),5)  
    pygame.draw.line(screen,black,(0,400),(600,400),5)
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, black)
                text_rect = text.get_rect(center=(col*200 + 100, row*200 + 100))
                screen.blit(text, text_rect)

    # show result if game over
    if game_over and winner:
        msg_font = pygame.font.Font(None, 50)
        if winner == "Draw":
            msg = "Draw - press R or click to reset"
        else:
            msg = f"{winner} wins - press R or click to reset"
        msg_surf = msg_font.render(msg, True, black)
        screen.blit(msg_surf, msg_surf.get_rect(center=(300, 550)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // 200
            col = mouse_x // 200
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
                board[row][col] = player
                winner = check_winner(board)
                if winner:
                    game_over = True
                else:
                    player = "O" if player == "X" else "X"

        # reset after game over
        if (event.type == pygame.MOUSEBUTTONDOWN and game_over) or (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
            player = reset_board()
            game_over = False
            winner = None

    pygame.display.flip()
pygame.quit()



