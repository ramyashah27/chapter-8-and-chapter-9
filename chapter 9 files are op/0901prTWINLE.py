f=open('poems.txt')
a=f.read()
if 'twinkle' in a:
    print('twinkle is present')
else:
    print('no twinkle is not present')
f.close()