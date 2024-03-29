import random
import pyperclip
import os

print("Installing Dependencies...")
os.system("pip install pyperclip")
os.system("cls")

passlength = int(input("Enter your desired Password length: "))

if passlength > 72:
    print("Invalid Password length. Please enter a number between 1 and 72.")
    os.system("pause")

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
symbols = "!@#-$%*&_?"

combo = upper_case + lower_case + nums + symbols
passw = "".join(random.sample(combo, passlength))

print("Generated Password:", passw)
pyperclip.copy(passw)
print("")
print("Your password has automatically been copied to the Clipboard!")

print("")
input("Press Enter to Exit.")
