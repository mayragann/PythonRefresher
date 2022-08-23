
#Legal Driving Age

legal_driving_age = 16
user_age = float(input("Please enter your current age: "))

if(user_age >= legal_driving_age):
    print("You are legally able to drive")

else:
    print("You are not old enough to drive")


#Random Number


import random
random_number = 6

random_number = random.randint(0,10)
print(random_number)

if (random_number >= 0 and random_number<= 2):
    print('0 or 1 or 2')
elif (random_number >= 3 and random_number<= 5):
    print('3 or 4 or 5')
elif (random_number >= 6 and random_number<= 8):
    print('6 or 7 or 8')
elif (random_number >= 9 and random_number<= 10):
    print('9 or 10')



#Best Football team 

football_team = input('Which football team is the best? ')

if (football_team == 'Bears'):
    print('Quarterback much?')

elif (football_team == 'Vikings'):
    print('Loud noises!')
elif (football_team == 'Lions'):
    print('LOL! they bad!')
elif (football_team == 'Packers'):
    print('Best team in the world! Actually, the universe!')
else:
    print('Pick a different team')


# Loops Lab

for number in range(5):
    print('Hello')
 

for number in range(11):
    print(number)


for number1 in range(10,0,-1):
    print(number1)



user_count = int(input('How Many times do you want to run loop?: '))

for number in range (1, user_count + 1):
    print('devCodeCamp')

best_football_team = 'packers'

for character in best_football_team:
    print(character)



for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print('fizzbuzz')
        continue
    elif fizzbuzz % 3 == 0:
        print('fuzz')
        continue
    elif fizzbuzz % 5 == 0:
        print('buzz')
        continue
    print(fizzbuzz)



started = 0
hello_world = True

while hello_world is True:
    if started == 4:
        hello_world = False
        print('Hello!')

    else:
        started += 1
        print('Hello!')



print('Enter Correct Password')

attempts = 0
correct_password = True

while correct_password is True:
    password = input('Enter Password: ')
    if password == 'Hello!':
        print ('User Validated')
        break # break stops it from looping when correct answer put in
    else:
        print('try again')
        attempts += 1
    
