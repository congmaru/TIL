name = '콩'
score = 100

print('안녕 내 이름은 %s 야' %name)  #%s는 문자열을 의미. 뒤의 네임이 s로 들어간다
print('나는 %d 점짜리 강아지' %score) 


print(f'이름 : {name}, 점수 : {score}')


print(f'''
안ㄴ영 내 이름은
{name}
이야
''')

# string interpolation을 통해 출력형식 지정 뿐만 아니라, 연산도 가능합니다.
# pi = 3.141592를 할당하고 
# 원주율은 3.14. 반지를이 2일 때 원의 넓이는 12.566368이라고 출력해봅시다.

pi = 3.141592
print(f'{pi:.3}')
r = 2

print(f'원주율은 {pi}이고, 반지름이 {r}일 때 원의 넓이는 {pi*r**2}입니다.')