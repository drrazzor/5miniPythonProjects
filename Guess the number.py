#Guess the Number

import random;

rn = random.randint(1,3)
#print (rn)

Try=0
while(Try<3):
  userguess = input('Guess the number between 1 and 3');
  print(userguess);
  if (rn==userguess):
    print("CONGRATS");
  else:
    print("Try Again");
  Try = Try + 1;

