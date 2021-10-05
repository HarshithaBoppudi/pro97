import random
secretnumber = random.randint(1, 9)

chancesleft = 5

print("Guess a number b/w 1 to 9 : ")


for i in range(1, 6):
 
  guess = int(input("Take a guess: "))
  
  
  if guess < secretnumber:
    print("Guess is too low!")
  elif guess > secretnumber:
    print("Guess is too high!")
  else:
    
    break
print("Chances Left: " + str(chancesleft))
if guess == secretnumber:
    print("You guessed it right!")
else:
    print("You lose!")
    print("The number I thought was " + str(secretnumber))