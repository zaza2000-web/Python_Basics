def main():
    name = get_user_name()
    is_user_valid(name)
    





def get_user_name():
    get_name = input("Write your name: ")
    return get_name
    

def is_user_valid(user_name):
    while True:
        if isinstance(user_name,str) and user_name.isalpha():
            print(f"Welcome {user_name}")
            break
        else:
            user_name = get_user_name()

        

    



main()