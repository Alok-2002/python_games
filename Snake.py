import pygame as pg
from random import randrange

WINDOW = 770
pg.display.set_caption('SNAKE GAME')
TILES_SIZE = 40
RANGE = (TILES_SIZE // 2,WINDOW - TILES_SIZE // 2, TILES_SIZE)
get_random_position = lambda: [randrange(*RANGE),randrange(*RANGE)]
snake = pg.rect.Rect([0,0,TILES_SIZE - 2, TILES_SIZE - 2])
snake.center = get_random_position()
length = 1
segments =[snake.copy()]
snake_dir = (0,0)
time , time_step =0,150
food = snake.copy()
food.center =  get_random_position()
screen = pg.display.set_mode([WINDOW]*2)
clock = pg.time.Clock()
direction = {pg.K_w : 1,pg.K_s : 1,pg.K_a : 1,pg.K_d : 1}

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and direction[pg.K_w]:
                snake_dir = (0 , -TILES_SIZE)
                direction = {pg.K_w : 1,pg.K_s : 0,pg.K_a : 1,pg.K_d : 1}
            if event.key == pg.K_s and direction[pg.K_s]:
                snake_dir = (0 , TILES_SIZE)
                direction = {pg.K_w : 0,pg.K_s : 1,pg.K_a : 1,pg.K_d : 1}
            if event.key == pg.K_a and direction[pg.K_a]:
                snake_dir = (-TILES_SIZE , 0)
                direction = {pg.K_w : 1,pg.K_s : 1,pg.K_a : 1,pg.K_d : 0}
            if event.key == pg.K_d and direction[pg.K_d]:
                snake_dir = (TILES_SIZE , 0)
                direction = {pg.K_w : 1,pg.K_s : 1,pg.K_a : 0,pg.K_d : 1}
    screen.fill('black')
    #check boundaries and selfeating
    self_eating = pg.Rect.collidelist(snake,segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center , food.center = get_random_position(),get_random_position()
        length , snake_dir = 1 ,(0,0)
        segments = [snake.copy()]
    #check food position
    if snake.center == food.center:
        food.center = get_random_position()
        length +=1
    #draw food and snake
    pg.draw.rect(screen,'red', food)
    [pg.draw.rect(screen,'green',segment) for segment in segments]
    #moving the snake
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:] 
    pg.display.flip()
    clock.tick(60)
