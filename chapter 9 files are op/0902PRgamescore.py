
# def game():
#     num=int(input('enter the score: '))
#     return num
# score= game()
# with open('gamescore.txt') as f:
#     gameplayed = int(f.read())
# if gameplayed<score:
#     print('score updated in gamescore as your score is', score)
#     with open('gamescore.txt',"w") as f:
#         f.write(str(score))
# elif gameplayed<score:
#     print('score updated in gamescore as your score is', score)
#     with open('gamescore.txt',"w") as f:
#         f.write(str(score))
# else:
#     print('VERY LOW U STUPID')
    
def game():
    num=int(input('enter the score: '))
    return num
score= game()
with open('gamescore.txt') as f:
    gameplayed = (f.read())
if gameplayed=='':
    print('score updated in gamescore as your score is', score)
    with open('gamescore.txt',"w") as f:
        f.write(str(score))
elif int(gameplayed)<score:
    print('score updated in gamescore as your score is', score)
    with open('gamescore.txt',"w") as f:
        f.write(str(score))
else:
    print('VERY LOW U STUPID')