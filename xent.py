from sys import argv, dont_write_bytecode
dont_write_bytecode = True
from time import *
import os



def lex(v1):
    output = ""
    # list
    LIN = list(v1)
    # current character
    char = ""
    # string of data
    stri = ""
    # state of data
    state = 0
    # state 0: default state
    # state 1: string printing
    # state 2: comment
    # state 3: command runner
    # if in a string
    in_str = 0
    # location in LIN variable
    location = 0
    no_brk = 0
    cmd_run = ""
    
        
    args = argv[2:]
      
    # argument basic syntax
        
        
        
        
      
    #logic IF
      
    arg1 = ""
      
    arg2 = ""
    prev_char=""
    for char in LIN:
        location += 1

        stri += char
        #print (str)
        if char == " " and ( state == 0 or state == -1 ) and in_str == 0:
            stri = ""

        elif char == "!" and state == 0 and in_str == 0:
            stri = ""
        elif char == "\n" and state == 0 and in_str == 0:
            stri = ""
            # print
        elif stri == "PRINT" and state == 0:
            state = 1
            stri = ""
        elif stri == "print" and state == 0:        # in case somebody forgets capitals
            state = 1
            stri = ""
        elif (char == "\"" or char == "\'") and state == 1 and in_str == 0:
            in_str = 1
            stri = ""
        elif state == 1 and in_str == 1 and (char == "\"" or char == "\'"):
            in_str = 0
            print(stri[:-1])
            stri = ""
            state = 0
        # comments
        elif state == 0 and stri == "~":
            state = 2
            stri = ""
        elif state == 2 and char == "~":
            state = 0
            stri = ""
        
        
        
        #macros
        elif state == 0 and char == "%":
          #macro instator
          state = 3
          stri = ""
        elif state == 3 and char == "%":
          if len(stri) > 253194:
            print("WARNING:  macro is over or equal to 253,195 characters and is at risk of breaking xent, proceed with caution!\n press any key to continue")
            input()
            print("XenText: i sure hope you know what your doing")
            sleep(2)
          state = 0
          stri = ""
          stream = os.popen(cmd_run)
          strix = ""
          charx = ""
          for charx in stream.read():
            strix += charx
          print(strix)  
        elif state == 3:
          cmd_run += char
          stri = ""
        
        
        #breakpoint @brk
        elif state == 0 and no_brk == 0 and stri == "@brk":
          input("===")
          stri = ""
        elif state == 0 and no_brk == 0 and stri == "@nbrk":
          no_brk = 1
          stri = ""
        elif state == 0 and no_brk == 1 and stri == "@ybrk":
          no_brk = 0
          stri = ""
        
        #======================
        #previous character
        prev_char = char
# run definition
def run():
    gi = open(argv[1], "r")
    gi = gi.read()
    lex(gi)


run()
