#윤년판별

def leap_year(years):
    if (years % 4 == 0 and years %100 != 0) or years % 400 == 0: #코드를 줄일 수 있다.
        return True
    else:
        return False

# if leap_year(2021):
#     print('윤년입니다')
# else:
#     print('윤년이아닙니다.')

print('윤년입니다') if leap_year(2021) else print('윤년이아닙니다')