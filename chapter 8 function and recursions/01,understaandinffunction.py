def percentage150(marks):
    # p=(sum(marks)/150)*100
    p=(marks/80)*100
    return p
# marks=[20,30,50]
marks = int(input('enter the marks\n'))
if marks>80:
    print('this value is invalid u cant get extra marks for good handwriting')
else:
    percentage1 =percentage150(marks)
    persign="%"
    print(percentage1,persign)
