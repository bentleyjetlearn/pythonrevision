'''import random
secretnumber=random.randint(1,15)
while True: 
    guess=int(input('Enter a number between 1,15 '))
    if secretnumber==guess:
        print('You did it') 
        break
    elif secretnumber > guess:
        print('Your guess is low')
    elif secretnumber < guess:    
        print('Your guess is higher')'''
#atm project
amount=int(input('How much money do you want?'))
if amount%500==0:
    print('Take your money')
else: 
    print("Error! Only 500's please")
