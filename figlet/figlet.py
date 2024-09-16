import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        text = input("Write: ")
        random_font = random.choice(fonts)
        figlet.setFont(font = random_font)
        print(figlet.renderText(text))
    elif len(sys.argv) == 3 and  sys.argv[1] == "-f":
        font_name = sys.argv[2]
        if font_name in fonts:
            figlet.setFont(font = font_name)
            text = input("Write: ")
            print(figlet.renderText(text))
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Ussage")



main()
