from selenium import webdriver
import pyautogui, time
moder_index = input("Enter the moders'index:\n")
#pages = int(input('How many working pages it has?\n'))
fox = webdriver.Firefox()

fox.get(f'https://www.nexusmods.com/skyrim/users/{moder_index}?tab=user+images')

images = fox.find_elements_by_class_name('mod-image')

# create a list of links
links = []

def scanner():
	for image in images:
		link = image.get_attribute('href')
		links.append(link)

scanner()
	
for link in links:
	fox.get(link)
	time.sleep(2)
	pyautogui.press('f6')
	time.sleep(0.2)
	pyautogui.press('right')
	pyautogui.keyDown('shift')
	pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
	pyautogui.keyUp('shift')
	#time.sleep(0.5)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.5)
	source = fox.find_element_by_class_name('aligncenter').get_attribute('src')
	time.sleep(0.5)
	fox.get(source)
	time.sleep(2)
	pyautogui.hotkey('ctrl', 's')
	time.sleep(0.8)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(0.8)
	pyautogui.hotkey('alt', 's')
	#time.sleep(0.5)

fox.quit()