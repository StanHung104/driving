country = input('請輸入國家： ')
age = input('請輸入年齡： ')
age = int(age)
if country == '台灣':
    if age >= 18:
        print('您符合考駕照資格')
    else:
        print('您尚未符合考駕照資格')
elif country == '美國':
    if age >= 16:
        print('您符合考駕照資格')
    else:
        print('您尚未符合考駕照資格')