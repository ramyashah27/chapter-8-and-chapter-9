f = open("allcode.txt","r")#by deafault it tale "r "that is reading mode 
data = f.read(420)#in (read first 420 character) we can give no. to print it
print(data)
f.close()