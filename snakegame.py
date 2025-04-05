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
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      exit()
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_w:
        snake_dir = (0, -TITLE_SIZE)
      if event.key == pg.K_s:
        snake_dir = (0, TITLE_SIZE)
      if event. key == pg.K_a:
        snake_dir = (-TITLE_SIZE, 0)
      if event.key == pg.K_d:
        snake_dir = (TITLE_SIZE, 0)
        
  screen.fill('black')
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

 
