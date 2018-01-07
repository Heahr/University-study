#난수발생
import random
computer = random.randint(1,3)
#숫자입력
number = input('숫자입력 : ')
number = int(number)
if(computer > number):
    print('computer : ' , computer , '사람 : ' , number , '사람이 졌습니다');
elif(computer == number):
    print('비겼습니다.');
else:
    print('computer' , computer , '사람' , number , '사람이 이겼습니다');

print('가위 : 0, 바위 : 1 보 : 2')

if(number == 0):
    if(computer == 0):
        print('비겻습니다.');
    elif(computer == 1):
        print('컴퓨터가 이겼습니다.');
    else:
        print('사람이 이겻습니다.');
