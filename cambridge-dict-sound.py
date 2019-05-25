from selenium import webdriver
import urllib.request
word = input('Enter the word: ')

fox = webdriver.Firefox()

fox.get(f'https://dictionary.cambridge.org/dictionary/english/{word}')

buttons = fox.find_elements_by_class_name('circle.circle-btn.sound.audio_play_button')
sources = set()

for button in buttons:
	source = button.get_attribute('data-src-ogg')
	sources.add(source)

for source in sources:
	urllib.request.urlretrieve(f'https://dictionary.cambridge.org{source}', f'{word}.ogg')
	#print(source)
fox.quit()