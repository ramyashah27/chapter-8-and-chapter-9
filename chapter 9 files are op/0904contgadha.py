words=['gadha','jaiwish','kaddu']
with open('donkey.txt') as f:
    gadha=f.read()
# replacegali=input('enter the word u want too change for donkey\n')
for gando in words:
    jaiwish= gadha.replace(gando[1],'sdhas')
for gando in words:
    jaiwish= gadha.replace(gando[2],'sdhas')
for gando in words:
    jaiwish= gadha.replace(gando[3],'sdhas')
with open('donkey.txt','w') as f:
      f.write(jaiwish)