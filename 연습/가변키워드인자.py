def print_family_name(*parents, **pets):
    print("아버지 :", parents[0])
    print("어머니 :", parents[1])
    if pets:
        for title, name in pets.items():
            print('{}:{}'.format(title, name))

a=print_family_name('아부지', '어무이', dog='멍멍이', cat='냥냥이')

print(type(a))