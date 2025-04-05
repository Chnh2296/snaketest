import pygame as pg

from random import randrange

WINDOW = 1000
TITLE_SIZE = 50
RANGE = (TITLE_SIZE // 2, WINDOW - TITLE_SIZE // 2, TITLE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0, 0, TITLE_SIZE - 2, TITLE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_position()

screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      exit()
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_w and dirs[pg.K_w]: 
        snake_dir = (0, -TITLE_SIZE)
        dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
      if event.key == pg.K_s and dirs[pg.K_s]:
        snake_dir = (0, TITLE_SIZE)
        dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
      if event. key == pg.K_a and dirs[pg.K_a]:
        snake_dir = (-TITLE_SIZE, 0)
        dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
      if event.key == pg.K_d and dirs[pg.K_d]:
        snake_dir = (TITLE_SIZE, 0)
        dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}
        
       
        
  screen.fill('black')
  #giới hạn và selfeating
  self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
  
  if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
    snake.center, food.center = get_random_position(), get_random_position()
    length, snake_dir = 1, (0, 0)
    segments = [snake.copy()]
  #ăn
  if snake.center == food.center:
    food.center = get_random_position()
    length += 1
  #food
  pg.draw.rect(screen, 'red', food)
  #vẽ rắn
  [pg.draw.rect(screen, 'green', segment) for segment in segments]
  #di chuyển
  time_now = pg.time.get_ticks()
  if time_now - time > time_step:
    time = time_now
    snake.move_ip(snake_dir)
    segments.append(snake.copy())
    segments = segments[-length:]
  pg.display.flip()
  clock.tick(60)

 
