import random
def guess(x):
  a =1
  b=x
  randomN = random.randint(a,b)
  # print(randomN)
  guess=int(input("your guess:"))
  while(guess!=randomN):
    if (guess > randomN):
      print("Too high")
    elif(guess < randomN):
      print("Too Low")
    guess = int(input("your guess:"))
  print("success!")
def computerguess(x):
  low=1
  high=x
  feedback=''
  guess = 0
  while(feedback!='c'):
    guess = random.randint(low, high)
    feedback = input(f"is {guess} too high? (H), too low (L), or Correct(C)?").lower()
    if(feedback=='h'):
      high = guess-1
    elif(feedback=='l'):
      low = guess+1

  print(f"Gotcha your number is {guess}")
choice=int(input("Which One do you want to guess? : \n1.You\n2.The Computer\n:"))
if (choice == 1):
      x=int(input("guessing range: "))
      guess(x)
if (choice == 2):
      x=int(input("guessing range: "))
      computerguess(x)
