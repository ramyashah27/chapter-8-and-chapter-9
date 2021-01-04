def percentage150(marks):
    # p=(sum(marks)/150)*100
    p=(marks/marks2)*100
    return p
# marks=[20,30,50]
marks= int(input('enter numerator \n'))
marks2= int(input('enter denominator \n'))
if marks2<marks:
    print('invalid ')
else:
    percentage1 =percentage150(marks)
    persign="%"
    print(percentage1,persign)
