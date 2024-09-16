import sys
from pyfiglet import Figlet

def main():
    f = Figlet(font = 'slant')
    print(f.renderText("Hello"))

main()