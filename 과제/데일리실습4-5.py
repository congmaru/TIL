#4-5

words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}


wlst = words_dict.keys()
iwords_lst=[]

for word in wlst:
    if word[-1] in 'bmp':
        iwords_lst.append('im' + word)
    if word[-1] in 'l':
        iwords_lst.append('il' + word)
    if word[-1] in 'r':
        iwords_lst.append('ir' + word)
    else:
        iwords_lst.append('in' + word)

print(sorted(iwords_lst))
