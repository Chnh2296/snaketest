import pygame as pg

from random import randrange

WINDOW = 1000
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      exit()
  screen.fill('black')
  pg.display.flip()
  clock.tick(60)
