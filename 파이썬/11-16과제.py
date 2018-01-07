string = '''Once when I was six years old I saw a magnificent
picture in a book, called True Stories from Nature, about
the primeval forest. It was a picture of a boa constrictor in
the act of swallowing an animal. Here is a copy of the
drawing. In the book it said: "Boa constrictors swallow
their prey whole, without chewing it. After that they are
not able to move, and they sleep through the six months
that they need for digestion.“ I pondered deeply, then,
over the adventures of the jungle. And after some work
with a colored pencil I succeeded in making my first
drawing. My Drawing Number One. It looked something
like this:'''

space=string.count(' ')
enter=string.count('\n')
print('Words in String =',space+enter+1,'\n')
j=65
k = 97
a = 0
print('Counting Alphabets (Upper and Lower case letters)')
for a in range(26):
    count_Large = string.count(chr(j+a))
    count_Small = string.count(chr(k+a))
    COUNT = count_Large + count_Small
    '''
    print("Number of '",chr(j+a),"' :",count_Large)
    print("Number of '",chr(k+a),"' :",count_Small)
    '''
    print("'",chr(j+a),"' :",COUNT)
    
    

    
    
