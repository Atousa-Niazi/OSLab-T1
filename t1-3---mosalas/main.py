'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
"""   Atousa Niazi Abkoh 98440127-os lab - T1-3 - mosalas """

print (' please enter The size of the sides of a triangle az a ,b ,c :\n')
a=int(input())
b=int(input())
c=int(input())

if a+b>c:
    if a+c>b:
        if b+c>a:
            print("it's a triangle ." )
            
else:
    print("it's not a triangle !")