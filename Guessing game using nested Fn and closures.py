import random   
def Get_Range(grange):
    guess = random.randint(0,grange)
    guesses = 0
    def Check_win(ans):
        nonlocal guess
        nonlocal guesses
        if int(ans) == int(guess):
            print(f"U got it after {guesses} wrong guesses :DD")
        else:
            guesses += 1 
            if int(ans) > int(guess) :
                print("Too High")
            else:
                print("Too Low") 
            global x 
            x(int(input("Your guess : ")))
            
    return Check_win
x =  Get_Range(int(input("Guessing range : ")))
x(int(input("Your guess : ")))
