#! /usr/bin/env python

# this is the XenCLI, licenced under the PRSL-1.0 licence. see LICENSE.md
import os
import sys
from time import *
# this is where the XenText cli will be held
cmds = "help , exit , cmds" , "run" , "creators" # command names go here!

command = input("XentCLI: ")

# plain ol' input, simple keywords

if command == "help":    # this shows help message
  help = input("help topic: ") # see 'specific help topics for the topics!
  
elif command == "exit":  # exit
  sys.exit("exited xen")

elif command == "cmds":
  print(cmds)
  
elif command == "run":      # runs files
  file = input("file to run: ")
  os.system('python3 xent.py ' + file)  # file must exist or an errno error gets thrown
  
elif command == "creators":
  print("protechCEO and j-tech-foundation")
  
#-------------------------------------- SPECIFIC HELP TOPICS

if help == "macros":
  print("macros are Xen's way of running shell commands")
  sleep(2)
  print("example")
  sleep(2)
  print("!%#!/bin/bash")
  print("python3 xent.py macaroni.xt")
  print("%")
  sleep(1)
  print("you can find more examples at xendocs.glitch.me")

  
#-------------------------------------- REPEAT AND COMMAND NOT FOUND CODE
else:
  print("XentCLI: command not found")
  
os.system('python3 cli.py') # for looping, otherwise the script ends after each command

# © 2020- @ProTechCEO (17lwinn)