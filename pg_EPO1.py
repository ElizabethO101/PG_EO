import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.05)
time.sleep(1)
pg.hotkey('winleft','up')
pg.typewrite('https://www.google.com/docs/about/\n', .01)
time.sleep (2)
pg.click(704, 528, 1,)
time.sleep (3)
pg.click(855, 286, 1,)
time.sleep (1)
pg.click(623, 406, 1,)
time.sleep (1)
pg.typewrite('eoliver@gcds.net', .01)
time.sleep (1)
pg.click(820, 489, 1)
time.sleep (1)
pw=pg.password("enter password","title","","*")
pg.typewrite(pw,.04)
pg.hotkey('enter')
pw=""
time.sleep (1)
pg.click(855, 286, 1)
time.sleep (1)
pg.typewrite('Congratulations! Python rocks!', .01)



