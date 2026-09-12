import pygame
pygame.init()
screen =pygame.display.set_mode((800,600))
pygame.display.set_caption("Bouncing Ball3")
white=(255,255,255)

running =True
ball_x=400
ball_y=300
ball_radius=20
vel_x=1
vel_y=1
colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0)
]
paddle_x = 350
paddle_y = 550
paddle_width = 100
paddle_height = 15
paddle_speed = 60
color_index = 0

score = 0
font = pygame.font.Font(None, 40)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event .type== pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if paddle_x >= 0:
                        paddle_x -= paddle_speed
        
                if event.key==pygame.K_RIGHT:
                    if paddle_x + paddle_width <= 800:
                        paddle_x += paddle_speed 
    ball_x += vel_x
    ball_y += vel_y           
    screen.fill(white)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (20, 20))
    
    if ball_x +ball_radius >=800:
        vel_x = -vel_x
        color_index = (color_index + 1) % len(colors)
    if ball_x - ball_radius <=0:
        vel_x = -vel_x
        color_index = (color_index + 1) % len(colors)
           
    if ball_y-ball_radius <=0:
        vel_y = -vel_y
        color_index = (color_index + 1) % len(colors)
            
    if ball_y + ball_radius>=600:
        ball_y = 600 - ball_radius
        vel_y = -vel_y
        color_index = (color_index + 1) % len(colors)
     
    pygame.draw.rect(
    screen,
    (0, 0, 0),
    (paddle_x, paddle_y, paddle_width, paddle_height)
)      
    pygame.draw.circle(
    screen,
    colors[color_index],
    (ball_x, ball_y),
    ball_radius
)
    if ball_y + ball_radius >= paddle_y:
        if paddle_x <= ball_x <= paddle_x + paddle_width:
            vel_y = -vel_y
            score +=1
   
    pygame.display.update()
pygame.quit()