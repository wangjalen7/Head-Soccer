# Jalen Wang (zac9nk)
# Aditya Kumar (fsc4md)

# OVERALL DESCRIPTION
# The game we have decided to create is head soccer. Essentially, the game consists of two players that can move around and each goes
# after a ball on a playing field. The players use their body (head) to bump the ball around. On each side of the screen/field is a goal
# that each player aims to hit the ball into. If the ball is scored into the goal, the player that scored the goal will get a point on
# the scoreboard. The two players will play until a certain score is reached or until the timer runs out. The first player to reach a
# score of 5 wins, or if they have more points at the end of the time.

# 5 REQUIRED FEATURES
# USER INPUT
# The inputs from keys W,S, and D and the arrow keys will be used to control/move player 1 and player 2 for the game.
# START SCREEN
# The start screen will be put into place before the game is started. The game can be started by pressing "T" and then the SPACE button.
# GAME OVER
# The game will end when either the timer runs out or one player reaches a score of 5 and the game over screen is shown.
# SMALL ENOUGH WINDOW
# The camera will be set to 800 x 600 to satisfy the screen size requirements.
# GRAPHICS/IMAGES
# Graphics and images will be used to create the soccer field, soccer ball, and players in the game.

# 4 OPTIONAL REQUIREMENTS
# RESTART FROM GAME OVER
# After each game ends, the "R" button will be pressed to restart the game (goes back to the start screen).
# SPRITE ANIMATION
# The movement of the players will be animated for running using a sprite sheet.
# TIMER
# A timer wil be implemented for the game. Once the timer reaches zero the game will stop just like a real soccer game and the winner
# will be shown on the game over screen.
# TWO PLAYERS SIMULTANEOUSLY
# Two players will play against each other in the head soccer game. Both will be able to control their own characters and try to hit
# the soccer ball.

import pygame
import gamebox

camera = gamebox.Camera(800, 600)

# player 1 images
p1_images = gamebox.load_sprite_sheet('Brazil_SpriteSheet_New.png', 1, 3) # replace with sprite sheet and rows/columns of images
p1 = gamebox.from_image(100, 400, p1_images[0])
current_frame_p1 = 0
p1_move = False

# player 2 images
p2_images = gamebox.load_sprite_sheet('argentina.png', 1, 3) # replace with sprite sheet and rows/columns of images
p2 = gamebox.from_image(700, 400, p1_images[0])
current_frame_p2 = 0
p2_move = False

# ball image
ball = gamebox.from_image(400, 300, "soccer_ball.png")

# goal images
goal1 = gamebox.from_image(20, 500, "goal_2.jpg")
goal2 = gamebox.from_image(780, 500, "goal_1.PNG")
goal_post_left = gamebox.from_color(25, 405, "red", 100, 15)
goal_post_right = gamebox.from_color(775, 405, "red", 100, 15)

background = gamebox.from_image(372, 400, "soccer_field.jpg")

# variables
game_on = False
game_start = False
display_home_screen = False
x = True
time = 60
ball.xspeed = 0
ball.yspeed = 15
p1_score = 0
p2_score = 0

# player movements and ball movements
def handle_keys(keys):
    global game_on, game_start, x, current_frame_p1, current_frame_p2, p1_move, p2_move
    gravity = 10
    speed = 10
    p1_move = False
    p2_move = False

    if game_on:
        # keeps the ball on the screen and bouncing around when it touches things
        ball.move_speed()
        if ball.y < 600 and (not ball.touches(goal1) or not ball.touches(goal2)):
            ball.y += 2
        if ball.y >= 585:
            ball.y = 585
            ball.yspeed *= -1
        if ball.y < 0:
            ball.y = 0
            ball.yspeed *= -1
        if ball.x < 0:
            ball.x = 0
            ball.xspeed *= -1
        if ball.x > 800:
            ball.x = 800
            ball.xspeed *= -1
        if ball.y < 300:
            ball.y = 300
            ball.yspeed *= -1
    # bounces off the head when the player hits the ball
    if ball.touches(p1):
        ball.x = p1.x
        ball.y = p1.y - 66
        ball.xspeed = 20
        ball.move_speed()
    if ball.touches(p2):
        ball.x = p2.x
        ball.y = p2.y - 66
        ball.xspeed = -20
        ball.move_speed()
    if ball.bottom_touches(p1) or ball.bottom_touches(p2):
        ball.yspeed *= -0.5
    # cannot score goal off the top of the goal post
    if ball.touches(goal_post_right) or ball.bottom_touches(goal_post_left):
        ball.yspeed *= -1

    if pygame.K_t in keys:  # draws all the parts of the game, ready to play
        ball.x = 400
        ball.y = 300
        ball.xspeed = 0
        ball.yspeed = 15
        p1.x = 100
        p1.y = 400
        p2.x = 700
        p2.y = 400
        x = False
        game_start = True
    if pygame.K_SPACE in keys:  # starts the game, ball moves and players can move, score starts and timer runs
        game_on = True

    # player controls player 2 (right side)
    if pygame.K_RIGHT in keys and game_on:
        p2.x += speed
        p2_move = True
    if pygame.K_LEFT in keys and game_on:
        p2.x -= speed
        p2_move = True
    if pygame.K_UP in keys and p2.y == 550 and game_on:
        p2.y -= 125
        p2_move = True
    if p2.x > 800:
        p2.x = 800
    if p2.x < 0:
        p2.x = 0
    if p2.y > 550:
        p2.y = 550
    if p2.y < 550:
        p2.y += gravity
    # animation of player 2 running
    if p2_move:
        p2.image = p2_images[int(current_frame_p2)]
        current_frame_p2 += 0.5
        if current_frame_p2 > 2:
            current_frame_p2 = 0
    else:
        p2.image = p2_images[0] #standing still one

    # player controls player 1 (left side)
    if pygame.K_d in keys and game_on:
        p1.x += speed
        p1_move = True
    if pygame.K_a in keys and game_on:
        p1.x -= speed
        p1_move = True
    if pygame.K_w in keys and p1.y == 550 and game_on:
        p1.y -= 125
        p1_move = True
    if p1.x > 800:
        p1.x = 800
    if p1.x < 0:
        p1.x = 0
    if p1.y > 550:
        p1.y = 550
    if p1.y < 550:
        p1.y += gravity
    # animation of player 1 running
    if p1_move:
        p1.image = p1_images[int(current_frame_p1)]
        current_frame_p1 += 0.5
        if current_frame_p1 > 2:
            current_frame_p1 = 0
    else:
        p1.image = p1_images[0] #standing still one

# draws all the images and things for the game so you can see them
def draw_items():
    if game_start:
        camera.draw(goal_post_left)
        camera.draw(goal_post_right)
        camera.draw(background)
        camera.draw(p1)
        camera.draw(p2)
        camera.draw(ball)
        camera.draw(goal1)
        camera.draw(goal2)

# timer for the game
def timer():
    global p1_score, p2_score, game_on, game_start, time
    # draws timer when game starts
    if game_start:
        camera.draw(str(int(time)), 50, "black", 600, 30)
        if game_on and not int(time) == 0:
            time -= 1/35 # countdown for the timer
    # stops game when timer hits zero and displays the winner
    if int(time) == 0:
        game_start = False
        if p1_score > p2_score:
            camera.draw(("GAME OVER, P1 WINS"), 50, "black", 400, 30)
            camera.draw(("Press \"R\" to restart the game"), 50, "black", 400, 70)
        elif p2_score > p1_score:
            camera.draw(("GAME OVER, P2 WINS"), 50, "black", 400, 30)
            camera.draw(("Press \"R\" to restart the game"), 50, "black", 400, 70)
        else:
            camera.draw(("GAME OVER, TIE"), 50, "black", 400, 30)
            camera.draw(("Press \"R\" to restart the game"), 50, "black", 400, 70)

# score keeping for the game
def score_p():
    global p1_score, p2_score, game_on, game_start, display_home_screen
    # scoring points
    if ball.left_touches(goal1) and game_on:
        p2_score += 1
        game_on = False
    if ball.right_touches(goal2) and game_on:
        p1_score += 1
        game_on = False
    if game_start:
        camera.draw(gamebox.from_text(300, 50, str(p1_score), 50, "Red", bold=True))
        camera.draw(gamebox.from_text(500, 50, str(p2_score), 50, "Blue", bold=True))
    # stops the game when a player's score reaches 5
    if p1_score == 5:
        game_start = False
        display_home_screen = False
        camera.draw(("GAME OVER, P1 WINS"), 50, "black", 400, 30)
        camera.draw(("Press \"R\" to restart the game"), 50, "black", 400, 70)
    if p2_score == 5:
        game_start = False
        display_home_screen = False
        camera.draw(("GAME OVER, P2 WINS"), 50, "black", 400, 30)
        camera.draw(("Press \"R\" to restart the game"), 50, "black", 400, 70)

# restarts the game, resets everything
def restart(keys):
    global display_home_screen, p1_score, p2_score, game_on, game_start, time
    if pygame.K_r in keys:
        game_on = False
        game_start = False
        display_home_screen = True
        time = 60
        ball.xspeed = 0
        ball.yspeed = 15
        p1_score = 0
        p2_score = 0

# start screen
def home_screen():
    global game_on, game_start, display_home_screen, x
    # draws the start screen and all the rules
    if x:
        camera.draw(("HEAD SOCCER"), 50, "red", 400, 100)
        camera.draw("Jalen Wang", 25, "black", 400, 150)
        camera.draw("Rules: Use the W, A, and D keys and arrow keys for each player and try to hit the ball into the goal.", 25, "black", 400,
                    200)
        camera.draw("First to five wins or whoever has more points at the end of the timer.", 25, "black", 400, 225)
        camera.draw("Press \"T\" then \"SPACE\" to start the game and after every point to reset positions.", 25,
                    "black", 400, 300)
    if game_on == False and game_start == False and display_home_screen == True:
        camera.draw(("HEAD SOCCER"), 50, "red", 400, 100)
        camera.draw("Jalen Wang", 25, "black", 400, 150)
        camera.draw("Rules: Use the W, A, and D keys and arrow keys for each player and try to hit the ball into the goal.", 25, "black", 400,
                    200)
        camera.draw("First to five wins or whoever has more points at the end of the timer.", 25, "black", 400, 225)
        camera.draw("Press \"T\" then \"SPACE\" to start the game and after every point to reset positions.", 25,
                    "black", 400, 300)

def tick(keys):
    camera.clear("white")
    home_screen()
    handle_keys(keys)
    draw_items()
    timer()
    score_p()
    restart(keys)
    camera.display()

ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
