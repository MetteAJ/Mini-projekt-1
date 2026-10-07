import pygame
import math
from datetime import datetime
import random

# screen
screen_height = 480
screen_width = 640
radius = 200
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
    

# Hold vinduet åbent
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.Surface.fill(screen, (255, 255, 255))

    pygame.draw.circle(screen, (0, 150, 0), (screen_width // 2, screen_height // 2), radius, 5)

    # Minutstreger
    start = (screen_width/2, screen_height/2)
    length = radius
    angle = 0
    angle_offset = 360/12

    pygame.draw.circle(screen, (0, 119, 0), [screen_width/2, screen_height/2], radius)

    for line_counter in range(12):
        angle = line_counter * angle_offset
        x_offset = math.cos(math.radians(angle))*length
        y_offset = math.sin(math.radians(angle))*length
        end = (start[0] + x_offset, start[1] + y_offset)
        pygame.draw.line(screen, (255, 197, 211), start, end, 6)

    # Streger
    start = (screen_width/2, screen_height/2)
    length = screen_width/3.5
    angle = 0
    angle_offset = 360/12

    for line_counter in range(12):
        angle = line_counter * angle_offset
        x_offset = math.cos(math.radians(angle))*length
        y_offset = math.sin(math.radians(angle))*length
        end = (start[0] + x_offset, start[1] + y_offset)
        pygame.draw.line(screen, (0, 119, 0), start, end, 8)

    # tid
    now = datetime.now()
    seconds = now.second
    minutes = now.minute
    hours = now.hour

    viser_length_second = radius
    grad_sek = seconds * 6 - 90
    x = start[0] + viser_length_second * math.cos(math.radians(grad_sek))
    y = start[1] + viser_length_second * math.sin(math.radians(grad_sek))
    pygame.draw.line(screen, (255, 197, 211), start, (x,y), 2)

   
    viser_length_minute = radius - 30
    grad_min = ((minutes * 6) + (seconds * 0.1)) - 90
    x = start[0] + viser_length_minute * math.cos(math.radians(grad_min))
    y = start[1] + viser_length_minute * math.sin(math.radians(grad_min))
    pygame.draw.line(screen, (255, 197, 211), start, (x,y), 5) 

    viser_length_hour = radius - 50
    grad_hour = ((hours % 12) * 30) + (minutes * 0.5) - 90
    x = start[0] + viser_length_hour * math.cos(math.radians(grad_hour))
    y = start[1] + viser_length_hour * math.sin(math.radians(grad_hour))
    pygame.draw.line(screen, (255, 197, 211), start, (x,y), 8) 
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()