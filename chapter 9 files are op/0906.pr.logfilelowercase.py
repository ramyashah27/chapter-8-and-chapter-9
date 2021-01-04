with open('log.txt') as f:
    data=f.read()#.lower()==> THIS HElps in finding after the word is in captail or in in small letters
if 'ramya shah' in data.lower():
    print('yes')
else:
    print('no')