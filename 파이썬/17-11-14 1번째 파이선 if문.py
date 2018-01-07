#end=''을 사용할경우 내려가지 않고 계속 사용, 사용하지 않을 경우 내려간다.
'''
print('number: ',end='')
num = input()
number = int(num)
'''
'''
#숫자범위 지정하기.
#범위에 해당하면 판단할것인지, 해당하지 않으면 판단할것인지 결정해야한다.
if(1 <= number <= 10):
    if(number % 2 == 0):
        print(number, '-->짝수',end='')
        print('입니다.')
    else:
        print(number, '-->홀수')
else:
    print('plz try again')
print('end of program')
'''
'''
#다중 if 문 성적평가
if number >= 90:
    print('수');
elif number >= 80:
    print('우');
elif number >= 70:
    print('미');
elif number >= 60:
    print('양');
else:
    print('가');
'''
'''
#난수발생
import random
computer = random.randint(1,5)
#숫자입력
number = input('number = ? (1~5)')
number = int(number)

if(number == computer):
    print(number , computer , '일치');
else:
    print(number , computer , '불일치');
'''

#문자열에서 단어 검색: 포함여부,위치정보 출력
string = '''The Little Prince (French: Le Petit Prince; French pronunciation: ​[lə pəti pʁɛ̃s]), first published in 1943, is a novella, the most famous work of French aristocrat, writer, poet, and pioneering aviator Antoine de Saint-Exupéry.
The novella is one of the most-translated books in the world and was voted the best book of the 20th century in France. Translated into 300[3] languages and dialects,[4][5] selling nearly two million copies annually, and with year-to-date sales of over 140 million copies worldwide,[6] it has become one of the best-selling books ever published.[7][8][9][Note 2]
After the outbreak of the Second World War, Saint-Exupéry escaped to North America. Despite personal upheavals and failing health, he produced almost half of the writings for which he would be remembered, including a tender tale of loneliness, friendship, love, and loss, in the form of a young prince visiting Earth. An earlier memoir by the author had recounted his aviation experiences in the Sahara Desert, and he is thought to have drawn on those same experiences in The Little Prince.
Since its first publication, the novella has been adapted to numerous art forms and media, including audio recordings, radio plays, live stage, film, television, ballet, and opera.'''
#문자열 입력
word = input('단어입력:')
if(word in string):
    print('포함됨')
    print(word , '의 index' , string.find(word))
else:
    print('없음')

