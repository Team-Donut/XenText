import sys
from time import *
import os

os.system("clear")
print("--- Xent language installation ---")
print("")
print("requirements for installation:")
print("1. python3 +")
print("2. space to install")
print("3. wget, as the source will be written from there")
print("")
print("will install Xent 2.0 and XentCLI")
sleep(3)

install = input("ready to install? Y/N: ")

if install == "Y":
  print("getting source of Xent 2.0")
  sleep(2)
  os.system("wget https://getxent.glitch.me/xent.py")
  sleep(2)
  print("getting source of XentCLI 2.0")
  sleep(2)
  os.system("wget https://getxent.glitch.me/xentcli.py")
  
if install == "N":
  sys.exit("installation cancelled")
  