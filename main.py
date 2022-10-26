import pwinput
import os

clear = lambda: os.system("clear")

password = pwinput.pwinput(prompt='Enter Your Password: ', mask="*")