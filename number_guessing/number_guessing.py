import random
def main():
    random_num = random_number()
    while True:
        user_input = user_guess()
        if is_winner(user_input,random_num):
            print(f"Congrats you are winner, \n guessed number was: {user_input}")
            break
        else:
            pass
        




def random_number():
    numbers = random.randint(1,5)
    return numbers

def user_guess():
    guessed_number = int(input("Guess number from 1 to 5 and try to win against Random :): "))
    return guessed_number

def is_winner(guessed,random):
    return guessed == random
   
        
main()