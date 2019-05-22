from selenium import webdriver
import pyautogui, time

fox = webdriver.Firefox()
def page_changer(page_number):
    fox.find_element_by_id('select2-page_t-container').click()
    time.sleep(2)
    pyautogui.typewrite(f'{page_number}')
    pyautogui.press('enter')

def scanner():
    for image in images:
        link = image.get_attribute('href')
        links.append(link)

def downloader():
    for link in links:
        fox.get(link)
        time.sleep(1.5)
        pyautogui.press('f6')
        time.sleep(0.3)
        pyautogui.press('right')
        pyautogui.keyDown('shift')
        pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
        pyautogui.keyUp('shift')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        source = fox.find_element_by_class_name('aligncenter').get_attribute('src')
        time.sleep(0.5)
        fox.get(source)
        time.sleep(1.5)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(0.8)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.hotkey('alt', 's')

fox.get('https://www.nexusmods.com/skyrim/users/2913008?tab=user+images')

images = fox.find_elements_by_class_name('mod-image')

# create a list of links
links = []
scanner()
downloader()

fox.quit()