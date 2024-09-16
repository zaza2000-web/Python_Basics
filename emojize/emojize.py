import emoji

def main():
    user_input = input("Input: ")
    emojized = emoji.emojize(f"{user_input}", language="alias")
    print(emojized)

main()