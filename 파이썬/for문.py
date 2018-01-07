#반복문
'''
for number in [1,2,3,4,5,6,7,8,9,10]: ->>range(1,10); 가능
    print(number , end = '')
    if(number % 3) == 0:
        print('\n' , number, '--> 3의 배수')
else:
    print(number) #for끝
'''


#string = '''  fksajbdjkf skdb fas dkjfb asbf ka dbjfas jbfa dkjbfas dkj
# djfbsdk jfasd fakjs dfka sf bjaksd fjasbfjkasdb fkjsabdjkfbadsj
#    fqi bfqwbuiudbbjkfhasdbh chkhb kzb cjbjkfbhjb jbhqf hbfjs bfvb sfv be'''
#wordcnt = 0;
#for chr in string:
#    wordcnt = wordcnt + 1
#    print(chr , end= '')
#print('\n' , '총' , wordcnt , '문자')

'''
a = 0;
for number in range(1,10000+1):
    a += number
print(a);
'''

#이중 반복문
for i in range(1,3+1):
    for j in range(1,3+1):
        print(j , end='');
    print();
