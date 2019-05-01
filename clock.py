import datetime
now = datetime.datetime.now()
while now.minute != 0:
	now = datetime.datetime.now()
if now.minute == 59:
	answer = input("What is a game in which you answer question?\n")
	if answer.lower() == 'quiz':
		print("Good for you. This is correct")
	else:
		print('Think again...') 
	