#driving
country = input('請輸入國家')
age = int(input('請輸入年齡'))
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('不可以考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('不可以考駕照')
