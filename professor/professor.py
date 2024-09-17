import random



def main():
    level = get_level()
    score = 0

    for _ in range(10):

        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        print(f"{x} + {y} = ")

        chance = 0
        while chance < 3:
            try:
                user_answer = int(input("Answer: "))
                if user_answer == answer:
                    score += 1
                    break
                else:
                    chance +=1
                    if chance < 3:
                        raise(ValueError)
                    else:
                        print(f"correct answer was: {answer}")
            except ValueError:
                print("EEE")


    print(f"Your score is: {score}")

def get_level():
    while True:
        try:
            lvl = int(input("Choose lvl (1,2 or 3): "))
            levels = [1,2,3]
            if lvl in levels:
                return lvl
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError("Not correct lvl, choose (1,2 or 3)")


if __name__ == "__main__":
    main()
