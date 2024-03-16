import time
import pyautogui


def click1(img):
    # 仅点击一下相应图片位置#
    location = pyautogui.locateCenterOnScreen('img/'+img, confidence=0.7)
    # print(location)
    if location is not None:
        pyautogui.click(location)
    return location

def check(img):
    location = pyautogui.locateCenterOnScreen('img/' + img, confidence=0.7)
    if location is not None:
        print('查询到'+img)
    return location

def task_p():
    while check("stop_p.png") is None:
        time.sleep(4)
        click1("win_rate.png")
        click1("go.png")

def task_talk():
    # 进行对话任务
    click1()


def task_pin():
    # 进行 对话内 or 战斗内 页面拼点
    click1()


def task_select_guy():
    # 选择新人格加入队伍
    click1()


def task_enter():
    # 从bk入task
    w = click1('enter.png')
    if w is None:
        print("查找enter失败")

def task_check_num():
    pan1 = click1('to_battle_true.png')
    while pan1 is None:
        time.sleep(2)
        print("未找到to battle 激活状态")
        pan1 = click1('to_battle_true.png')
    print("已进入battle")
