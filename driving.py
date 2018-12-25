country = input('Where are you from? ')
age = input('How old are you? ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can drive the car.')
	else:
		print('You can not drive the car.')
elif country== 'USA':
	if age >= 20:
		print('You can drive the car.')
	else:
		print('You can not dive the car.')