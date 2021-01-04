def remove_and_strip(string,word):
    newstr=  string.replace(word,"   t")
    return newstr.strip()
    

this= ('        ramya is a good boy            ' )
n= remove_and_strip(this,"ramya ")
# print('this')
print(n)
# print(type(this))

