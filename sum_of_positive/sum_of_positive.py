def main():
    numbers = [123, -23, 215, -123, 1415, -135, 125, 1515, 'some', 'food', 13, 'all', -2]
    for number in numbers:
        if isinstance(number, str):
            continue
        if number < 1: 
            continue
        else:
            number += number
        print(number)
          

main()
