'''for i in range(10,0,-1):
    print (i)'''
    
#creating a chatbot
def chatbox():
    print("Welcome to Heng's restaurant, please enter your name.")
    name=input()
    print('Hello',name)
    order=input('Do you want to place your order-yes/no ')
    if order=='yes':
     food=input('Enter order details:')
     print('Thank you, your food will be ready soon')
    else:
       print('Good bye')
chatbox()

#area function
def area(l,b):
   if l==b:
      print('Area of square',l*b)
   else:
      print('Area of rectangle',l*b)
area(5,6)      
