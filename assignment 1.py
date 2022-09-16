#world puzzle game

def puzzle():
    correct=['iron man','captain america','hulk','antman','spider man']
    import random
    score=0
    for name in correct:
        temp=random.sample(name,k=len(name))
        inp=input('enter a word using the letters:{}'.format(temp))
        if inp==name:
            score+=1
        else:
            score-=1
    print('your total score is:',score)

puzzle()
