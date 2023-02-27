
import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Set the background color
background_color = (255, 255, 255)
window.fill(background_color)

# Initialize the game
player1_score = 0
player2_score = 0

# Create the game objects
player1 = pygame.Rect(40, window_height/2 - 50, 20, 100)
player2 = pygame.Rect(window_width - 60, window_height/2 - 50, 20, 100)
ball = pygame.Rect(window_width/2 - 10, window_height/2 - 10, 20, 20)

# Initialize the movement of the ball
ball_speed_x = 7
ball_speed_y = 7

# Initialize the movement of the players
player1_speed = 0
player2_speed = 0

# Main game loop
while True:

    # Listen for events from the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_speed = -7
            if event.key == pygame.K_DOWN:
                player1_speed = 7
            if event.key == pygame.K_w:
                player2_speed = -7
            if event.key == pygame.K_s:
                player2_speed = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1_speed = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player2_speed = 0

    # Update the position of the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce the ball off the edges
    if ball.top <= 0 or ball.bottom >= window_height:
        ball_speed_y *= -1

    # Check if the ball has gone off the edge
    if ball.left <= 0:
        player2_score += 1
        ball.center = (window_width/2, window_height/2)
        ball_speed_x = 7
        ball_speed_y = 7
    if ball.right >= window_width:
        player1_score += 1
        ball.center = (window_width/2, window_height/2)
        ball_speed_x = -7
        ball_speed_y = 7

    # Move the players
    player1.y += player1_speed
    player2.y += player2_speed

    # Make sure the players don't go off the edge
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= window_height:
        player1.bottom = window_height
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= window_height:
        player2.bottom = window_height

    # Draw the game objects
    pygame.draw.rect(window, (255, 0, 0), player1)
    pygame.draw.rect(window, (0, 255, 0), player2)
    pygame.draw.rect(window, (0, 0, 0), ball)

    # Draw the scores
    font = pygame.font.SysFont("roboto", 32, bold=True)
    player1_text = font.render(str(player1_score), 1, (255, 0, 0))
    player2_text = font.render(str(player2_score), 1, (0, 255, 0))
    window.blit(player1_text, (window_width/4 - player1_text.get_width()/2, 10))
    window.blit(player2_text, (3*window_width/4 - player2_text.get_width()/2, 10))

    # Update the window
    pygame.display.update()