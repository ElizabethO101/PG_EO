import pyautogui as pg
import time

pg.position (1102,34)
pg.click(1102, 34, 1,)
time.sleep (1)
pg.typewrite('classroom', .01)
pg.typewrite(['enter'], .1)
time.sleep (1)
pg.click(1043, 382, 1,)
time.sleep (1)
pg.click(1025, 426, 1,)
time.sleep (3)
pg.click(1200, 292, 1,)
time.sleep (1)
pg.click(933, 414, 1,)
time.sleep (1)
pg.typewrite('eoliver@gcds.net', .01)
time.sleep (1)
pg.click(1167, 496, 1,)

