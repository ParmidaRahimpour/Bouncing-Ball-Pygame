import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing Ball2")

# رنگ‌ها
white = (255, 255, 255)
red_color = (255, 0, 0)
black = (0, 0, 0)

# موقعیت توپ
ball_x = 400
ball_y = 300

# اندازه توپ
ball_radius = 20

# سرعت توپ
vel_x = 5
vel_y = 5

# میزان قرمز شدن صفحه
red = 0

# فونت
font = pygame.font.Font(None, 60)

running = True

while running:

    # بررسی Eventها
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # حرکت توپ
    ball_x += vel_x
    ball_y += vel_y

    # برخورد با دیوار راست
    if ball_x + ball_radius >= 800:
        vel_x = -vel_x
        red = min(red + 10, 255)

    # برخورد با دیوار چپ
    if ball_x - ball_radius <= 0:
        vel_x = -vel_x
        red = min(red + 10, 255)

    # برخورد با دیوار بالا
    if ball_y - ball_radius <= 0:
        vel_y = -vel_y
        red = min(red + 10, 255)

    # برخورد با دیوار پایین
    if ball_y + ball_radius >= 600:
        vel_y = -vel_y
        red = min(red + 10, 255)

    # رنگ پس زمینه
    background_color = (
        red,
        255 - red,
        255 - red
    )

    screen.fill(background_color)

    # رسم توپ
    pygame.draw.circle(
        screen,
        red_color,
        (ball_x, ball_y),
        ball_radius
    )

    # اگر صفحه کاملاً قرمز شد
    if red == 255:

        text = font.render(
            "DONE!",
            True,
            white
        )

        screen.blit(
            text,
            (330, 270)
        )

    pygame.display.update()

pygame.quit()