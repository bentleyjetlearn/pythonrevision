'''x=6
print(x)
print(type(x))
a='Hi my name is Bentley. I am 12 years old.' 
print(a)
print(type(a))
b=2.95
print(b)
print(type(b))
print(x<b)
a_1=2
name=input('Enter your name ')
print('Hello',name)

#drawing a square
import turtle
pen=turtle.Turtle()
pen.color('blue')
for i in range(4):
    pen.forward(100)
    pen.right(90)
#turtle.mainloop()    
for i in range(1,11,3):
 print(i)

for i in range(2,20,2):
    print(i)

#while loop
i=1
while i<=30:
    print (i)
    i=i+2

# conditionals
for i in range(1,31):
    if i%3==0:
        print ('Bingo')
    else:
        print(i)'''

#student grades 
math=int(input('enter marks in math:'))
geography=int(input('enter marks in geography:'))
italian=int(input('enter marks in italian:'))
percent=(math+geography+italian)/300*100
print(percent)
if percent >95:
    print('A grade')
elif percent >80:
    print('B grade')
elif percent >70:
    print('C grade')  
else:
    print('D grade')      