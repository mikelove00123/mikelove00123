#copybot.py
'''
1.ใช้เมาส์คลิปไปยังตำแหน่งที่ต้องการcopy
Point(x=619, y=231)
pg.click(start_point)
2.ลากไปให้สุดบรรทัด
pg.drag(707,234)
3.กดปุ้ม CTRL+C
4.ขยับเมาส์ไปทางด้านซ้าย
Point(x=131, y=219)
5.กดCTRL+Vแก้วกดENTER
'''

import pyautogui as pg
import time

def copytext(nextline=0):
    ##################line1############
    time.sleep(0.1) #รอ1วิ
    start_point = (619,231 + nextline) 
    pg.click(start_point)

    time.sleep(0.1)
    end_point = (707,234)
    pg.dragTo(end_point,duration=0.1)

    pg.hotkey('ctrl','c')

    left_notepad = (131,219)
    pg.click(left_notepad)
    pg.hotkey('ctrl','v')
    #pg.press('enter')
copytext()
copytext(17)
'''
##################line2############
time.sleep(0.1) #รอ1วิ
start_point = (619,253) 
pg.click(start_point)

time.sleep(0.1)
end_point = (707,253)
pg.dragTo(end_point,duration=0.1)

pg.hotkey('ctrl','c')

left_notepad = (131,219)
pg.click(left_notepad)

pg.press('down')
pg.hotkey('ctrl','v')
pg.press('enter')

##################line3############
time.sleep(0.1) #รอ1วิ
start_point = (619,269) 
pg.click(start_point)

time.sleep(0.1)
end_point = (707,269)
pg.dragTo(end_point,duration=0.1)

pg.hotkey('ctrl','c')

left_notepad = (79,276)
pg.click(left_notepad)
pg.press('down')
pg.hotkey('ctrl','v')
pg.press('enter')

##################line4############
time.sleep(0.1) #รอ1วิ
start_point = (619,288) 
pg.click(start_point)

time.sleep(0.1)
end_point = (707,288)
pg.dragTo(end_point,duration=0.1)

pg.hotkey('ctrl','c')

left_notepad = (76,290)
pg.click(left_notepad)
pg.press('down')
pg.press('down')
pg.hotkey('ctrl','v')
pg.press('enter')
'''