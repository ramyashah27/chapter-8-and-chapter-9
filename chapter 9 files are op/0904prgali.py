with open('donkey.txt') as f:
    jaiwish=f.read()
replacegali=input('enter the word u want too change for donkey\n')
jaiwish= jaiwish.replace('donkey',replacegali)
with open('donkey.txt','w') as f:
      f.write(jaiwish)