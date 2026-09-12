import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
white=(255,255,255)
screen.fill(white)
ball_x=400
ball_y=300
ball_radius=20
vel_x=5
vel_y=5
running =True
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]
color_index = 0

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
    ball_x += vel_x
    ball_y += vel_y
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
        vel_y = -vel_y
        color_index = (color_index + 1) % len(colors)

    pygame.draw.circle(screen,colors[color_index],(ball_x,ball_y),ball_radius)
    font = pygame.font.Font(None, 50)
    text = font.render("Hello world!", True, (0, 0, 0))
    screen.blit(text, (300, 250))
    pygame.display.update()
pygame.quit()