import os
oldname ="sample2.txt"
newname="newsample.txt"
with open ('oldname') as f:
    data=f.read()
with open ('newname.txt') as t:
    t.write(data)
os.remove(oldname)