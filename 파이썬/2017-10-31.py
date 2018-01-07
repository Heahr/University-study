#숫자를 입력 받아서
#몫과 나머지 출력

#1. 변수선언:입력 숫자를 저장.
number = 0
quotient = 0
remainder = 0

#2. 숫자를 입력 받음
number = input('숫자=?')
number = int(number) #숫자형 수치

#3. 나머지 변수:나머지 저장
remainder = number % 3

#4. 몫 변수:몫을 저장함.
quotient = int(number) // 3

#5. 출력:10의 몫 3, 나머지 1
print(number, '의 몫:', quotient, ',', '나머지:', remainder)
