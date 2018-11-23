#python program to find the score and winner of 'The Minion Game'.

print('please enter string in uppercase')
string= (input()).upper()#input a string
vowels = 'AEIOU'.upper()
kevin = 0#initializing score by zero
staurt = 0
for i in range(len(string)):#it iterates through the length of string
    if string[i] in vowels:#if the string contains a vowel kevin is assigned the score
        kevin += (len(string) - i)
    else:
        staurt += (len(string) - i)
if kevin > staurt:
    print('kevin', kevin)
elif staurt > kevin:
    print('stuart', staurt)
else:
    print('draw')