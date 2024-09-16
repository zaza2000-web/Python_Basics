import emoji

def main():
    text = input("Write emoji like: :thumbsup: ")
    emojized = emoji.emojize(f"{text}", language = "alias")
    print(emojized)
 

main()