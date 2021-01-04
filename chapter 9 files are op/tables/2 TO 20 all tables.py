# for i in range(2,11):
#     with open(f"table of {i}.txt",'w') as f:
#         for t in(1,21):
#             with open(f"table of {i}.txt",'w') as f:
#                 f.write(f'{i}X{t}={i*t}')
num=int(input('enter the number u wanna make: '))
if num<20:
    for i in range(2,num+1):
        with open(f"tables/table of {i}.txt",'w') as f:
            for t in range(1,11):
                f.write(f'{i}X{t}={i*t}\n')
else:
    print('ur computer space may fill up so sorry STUPID')