# f = open('another.txt', 'w')
# f.write("this file is created through writing in 'w'")
# f.close()
# this is to make/open file and will add (write) all data in it, it will overright

f = open('another.txt', 'a')
f.write(' and this is appending')
f.close()
#this is to add data in the end 
# how many times we run the program each time the data in write will add in the end