import sys
import time

import pyautogui

import task
import block

# 初始化检测
ci = 0
flag = 1
while flag == 1:
    time.sleep(0.5)
    print(ci)
    ci = ci + 1
    # 进入bk页面
    block.bk_check()
    # 结束检测
    if ci > 18:
        break
    # final = pyautogui.locateOnScreen()

# ci = 0
# while True:
#     c1('img/test.jpg')
#     ci = ci + 1
#     print(ci)
#     if ci > 1:
#         sys.exit()
