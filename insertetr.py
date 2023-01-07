import webbrowser
import mouse
import time
import keyboard


ep_links = []
what_paste = []

def links_gen(ep_pro,serie_cnt):
    for index in range(1,serie_cnt+1):
        ep_link = ep_pro.replace('$',str(index+158))
        ep_links.append(ep_link)

def page_opner_and_editer_opner(page_link):
    webbrowser.open(page_link)
    time.sleep(7)
    mouse.move(997, 115)
    mouse.click('left')
    time.sleep(7)

def actioner(links_copied):
    mouse.wheel(-7)
    time.sleep(1)
    mouse.move(252, 295)
    time.sleep(1)
    mouse.click('left')
    time.sleep(1)
    mouse.move(254, 419)
    mouse.click('left')
    time.sleep(1)
    mouse.move(627,483)
    mouse.click('left')
    time.sleep(1)
    links = links_copied.split('\n')
    for i in links:
        keyboard.write(i)
        keyboard.press('enter')
        keyboard.release('enter')
    time.sleep(5)
    mouse.move(1046,582)
    time.sleep(1)
    mouse.click('left')
    time.sleep(2)
    mouse.wheel(-30)
    time.sleep(3)
    mouse.move(1124,633)
    time.sleep(3)
    mouse.click('left')
    time.sleep(7)
    keyboard.press('ctrl + w')
    keyboard.release('ctrl + w')
    time.sleep(5)


def get_links(file_name):
    topaste = ''
    file = open(file_name+'.txt','r')
    file = file.readlines()
    for line in file:
        if 'that was ep number' in line:
            what_paste.append(topaste)
            topaste = ''
        else:
            topaste += line
ep_cnts = int(input('enter how many eps exist : '))
links_gen(input('enter the episode prototype with $ : '),ep_cnts)
get_links(input('enter the file name without the end : '))
for i in range(0,ep_cnts):
    page_opner_and_editer_opner(ep_links[i])
    actioner(what_paste[i])


