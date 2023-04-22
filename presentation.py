import pyautogui

def presentation():
    pyautogui.moveTo(300, 54, 1.5)
    pyautogui.doubleClick(300, 54)
    pyautogui.typewrite('https://www.canva.com/design/DAFgRSoKthg/9EFh0V5LrGcAjCVrPpzE6A/edit')
    pyautogui.press('Enter')
    pyautogui.sleep(15)
    pyautogui.hotkey('Ctrl','Alt','p')

presentation()