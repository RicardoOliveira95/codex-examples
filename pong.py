import pygame 
import random 

# initialize pygame 
pygame.init() 

# create main window 
screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Paddle Game") 

# set up game variables 
# positions 
ball_pos = [400, 300] 
paddle1_pos = [0, 250] 
paddle2_pos = [780, 250] 

# speed of ball and paddles 
ball_speed = [2, 2] 
paddle1_speed = 0
paddle2_speed = 0

# scores 
player1_score = 0
player2_score = 0

# game loop 
running = True
while running: 
	# set background color 
	screen.fill((0, 0, 0)) 

	# draw paddles and ball 
	pygame.draw.rect(screen, (255, 255, 255), (paddle1_pos[0], paddle1_pos[1], 20, 100)) 
	pygame.draw.rect(screen, (255, 255, 255), (paddle2_pos[0], paddle2_pos[1], 20, 100)) 
	pygame.draw.circle(screen, (255, 255, 255), (ball_pos[0], ball_pos[1]), 10) 

	# draw score 
	font = pygame.font.Font(None, 50) 
	score1 = font.render(str(player1_score), 1, (255, 255, 255)) 
	screen.blit(score1, (350, 10)) 
	score2 = font.render(str(player2_score), 1, (255, 255, 255)) 
	screen.blit(score2, (450, 10)) 

	# update ball position 
	ball_pos[0] += ball_speed[0]
	ball_pos[1] += ball_speed[1]

	# check for wall collision 
	if ball_pos[1] <= 0 or ball_pos[1] >= 590: 
		ball_speed[1] = -ball_speed[1] 

	# check for paddle collisions 
	if ball_pos[0] <= 120 and paddle1_pos[1] < ball_pos[1] < paddle1_pos[1] + 100: 
		ball_speed[0] = -ball_speed[0] 
	if ball_pos[0] >= 680 and paddle2_pos[1] < ball_pos[1] < paddle2_pos[1] + 100: 
		ball_speed[0] = -ball_speed[0] 

	# update paddle positions 
	paddle1_pos[1] += paddle1_speed 
	paddle2_pos[1] += paddle2_speed 

	# check for paddle boundary 
	if paddle1_pos[1] <= 0: 
		paddle1_pos[1] = 0 
	if paddle1_pos[1] >= 500: 
		paddle1_pos[1] = 500 
	if paddle2_pos[1] <= 0: 
		paddle2_pos[1] = 0 
	if paddle2_pos[1] >= 500: 
		paddle2_pos[1] = 500 

	# check for goal 
	if ball_pos[0] < 0: 
		player2_score += 1 
		ball_pos = [400, 300] 
		ball_speed = [random.choice([-.4, .4]), random.choice([-.4, .4])] 
	if ball_pos[0] > 800: 
		player1_score += 1 
		ball_pos = [400, 300] 
		ball_speed = [random.choice([-.4, .4]), random.choice([-.4, .4])] 

	# handle events 
	for event in pygame.event.get(): 
		# quit game 
		if event.type == pygame.QUIT: 
			running = False 

		# move paddles 
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_UP: 
				paddle2_speed = -.4
			if event.key == pygame.K_DOWN: 
				paddle2_speed = .4
			if event.key == pygame.K_w: 
				paddle1_speed = -.4
			if event.key == pygame.K_s: 
				paddle1_speed = .4

		if event.type == pygame.KEYUP: 
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
				paddle2_speed = 0
			if event.key == pygame.K_w or event.key == pygame.K_s: 
				paddle1_speed = 0

	# update the screen 
	pygame.display.update() 

# quit game 
pygame.quit()