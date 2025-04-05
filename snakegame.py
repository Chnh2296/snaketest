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

screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      exit()
  screen.fill('black')
  [pg.draw.rect(screen, 'green', for segment in segments]
  pg.display.flip()
  clock.tick(60)
