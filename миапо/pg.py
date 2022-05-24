import pygame as pg
import sys
 
sc = pg.display.set_mode((300, 200))
 
# здесь будут рисоваться фигуры
 
pg.display.update()
 
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.time.delay(1000)