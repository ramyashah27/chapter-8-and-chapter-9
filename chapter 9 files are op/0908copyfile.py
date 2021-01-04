with open('this.txt') as f:
    copy=f.read()
with open('copythis.txt','w') as t:
    t.write(copy)