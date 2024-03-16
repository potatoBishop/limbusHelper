import time

import task
import pyautogui
import tkinter

list_img = [
            'img/sword.png']
    # ,
    #         'img/double_sword.png',
    #         'img/blood.png',
    #         'img/new_guy.png',
    #         'img/level_up.png',
    #         'img/boss.png',
    #         'img/loss.png']

def bk_check():
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()

    p_location = pyautogui.locateCenterOnScreen("img/stop_p.png", confidence=0.6)
    print(p_location)


    for img_item in list_img:
        location = pyautogui.locateOnScreen(img_item, region=(p_location.x, p_location.y + height/3, width/3, height), confidence=0.6)
        if location is not None:
            # 找到相应按钮 and 点击
            pyautogui.click(location)
            # 进入事件处理
            task.task_enter()
            if img_item == "img/sword.png":
                bk_sword()
            elif img_item == "img/double_sword.png":
                bk_double_sword()
            elif img_item == "img/blood.png":
                bk_blood()
            elif img_item == "img/new_guy.png":
                bk_new_guy()
            elif img_item == "img/level_up.png":
                bk_level_up()
            elif img_item == "img/boss.png":
                bk_boss()
            elif img_item == "img/loss.png":
                bk_loss()
            return
    print("没找到")

def bk_sword():
    # 单剑战斗
    print("进入单剑战斗")
    # click1()
    time.sleep(1)
    task.task_enter()
    time.sleep(1)
    task.task_check_num()
    time.sleep(1)
    task.task_p()

def bk_double_sword():
    # 双剑战斗
    task.click1()


def bk_blood():
    # 回血
    task.click1()


def bk_new_guy():
    # 新人格
    task.click1()


def bk_level_up():
    # 人格升级
    task.click1()


def bk_boss():
    # 关底boss
    task.click1()

def bk_loss():
    # 掉线 retry
    task.click1()