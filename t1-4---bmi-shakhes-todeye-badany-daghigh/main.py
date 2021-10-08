'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

"""   Atousa Niazi Abkoh 98440127-os lab - T1-4 - BMI shakhes todeye badany-daghigh """
# rasty ostad shekle to tamrin dar Obese eshkal dasht 24.9 bayad 34.9 bashad , bakhshe '<' va '>' ham bar aks neveshte bod .!!!

print ('please enter your weight by Kg and height by metre :\n')
print('weight : ')
w=float(input())
print('height : ')
h=float(input())
b=round((w/h**2),1)
print('\n your BMI is ',b)

if b<18.5:
    print('you are under weight ⚠!')
elif b>=18.5 and b<=24.9:
    print('you are normal ✔')
elif b>24.9 and b <=29.9:
    print('you are over weight !')
elif b>29.9 and b <=34.9:
    print('you are Obese ⚠ !!')
elif b>34.9 :
    print('you are extremely Obese ☠ !!!')

