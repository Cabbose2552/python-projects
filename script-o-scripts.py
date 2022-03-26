import time
import random
import math
import operator
from tkinter import *

pyver = '3.10.2'
version = '1.0.0'
cnt = 1
mlt = 2
mltnum = 1

while True:
        script = input("what script would you like? type list to display a list of scripts:")

        if script == ("list"):
                print("-----------------------------------------------------------------")
                print("|blink, plays a simple blinking animation                       |")
                print("|                                                               |")
                print("|cnt, counts to infinity                                        |")
                print("|                                                               |")
                print("|info, display info about script                                |")
                print("|                                                               |")
                print("|run skyrim, does what it says                                  |")
                print("|                                                               |")
                print("|clear, clears screen(mostly)                                   |")
                print("|                                                               |")
                print("|mlt, displays numbers multiplied by the entered value          |")
                print("|                                                               |")
                print("|stress-test-1/2, provides a simple stress test for your system.|")
                print("|                                                               |")
                print("|win, creates a window with the entered mesurements             |")
                print("|                                                               |")
                print("|xgen, generates a random xbox gift card code                   |")
                print("|                                                               |")
                print("|pgen, generates a random playstation gift card code            |")
                print("|                                                               |")
                print("|sgen, generates a random steam gift card code                  |")
                print("-----------------------------------------------------------------")

        elif script == "cnt":
            while True:
                cnt = cnt + 1
                print(cnt)
                
        elif script == ("cnto"):
            while True:
                strt = int(input("input number to count from:"))
                numi = int(input("input number to count to:"))

                print(strt)
                for x in range(numi-strt):
                    print(strt+1)
                    strt = strt+1

        elif script == ("xgen"):
                print("")
                nn = input("how many codes would you like:")
                print("")
                n = int(nn)
                def g(rolls):
                        data = "qwrtypdfghjkzxcvbnm2346789"
                        result = ""
                        while rolls >= 1:
                            c = random.choice(data)
                            result = c + result
                            rolls = rolls - 1
                        return result

                for x in range(n):
                        print(g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5))
                print("")
        elif script == ("sgen"):
                print("")
                nn = input("how many codes would you like:")
                print("")
                n = int(nn)
                def g(rolls):
                        data = "qwrtypdfghjkzxcvbnm2346789"
                        result = ""
                        while rolls >= 1:
                            c = random.choice(data)
                            result = c + result
                            rolls = rolls - 1
                        return result

                for x in range(n):
                        print(g(4)+"-"+g(6)+"-"+g(5))
                print("")
        elif script == ("pgen"):
                print("")
                nn = input("how many codes would you like:")
                print("")
                n = int(nn)
                def g(rolls):
                        data = "qwrtypdfghjkzxcvbnm234678923467892346789"
                        result = ""
                        while rolls >= 1:
                            c = random.choice(data)
                            result = c + result
                            rolls = rolls - 1
                        return result

                for x in range(n):
                        print(g(4)+"-"+g(4)+"-"+g(4))
                print("")

        elif script == ("mlt"):
            print("")
            mltnum = input("enternumber to mupltiply by:")
            print("")
            mltnumint = int(mltnum)
            while True:
                mlt= mlt * mltnumint
                print(mlt)

        elif script == ("info"):
                print("======================")
                print("author: nathan nolan||")
                print("======================")
                print("version:", version, "     ||")
                print("======================")
                print("python ver:", pyver, " ||")
                print("======================")
                
        elif script == ("stress-test-1"):
            while True:
                mlt= mlt * 99999999999
                print(mlt)
                
        elif script == ("stress-test-2"):
            while True:
                mlt= mlt * mlt
                print(mlt)

        elif script == ("blink"):
                for x in range(10):
                        print("-w-")
                        time.sleep(0.1)
                        print("owo")
                        time.sleep(0.1)
                        print("OwO")
                        time.sleep(0.1)
                        print("owo")
                        time.sleep(0.1)

        elif script == ("clear"):
            for x in range(50):
                    print("")

        elif script == ("run skyrim"):
                print("*faint dying sounds*")
                time.sleep(10)
                int("working")

        elif script == ("win"):
            winw = input("window width:")
            winh = input("window height:")
            # declare the window
            window = Tk()
            # set window title
            window.title("Python GUI App")
            # set window width and height
            window.configure(width=winw, height=winh)
            # set window background color
            window.configure(bg='lightblue')
            window.mainloop()
        elif script == ("mathops"):
                ops = {'+':operator.add,
                    '-':operator.sub,
                    '*':operator.mul,
                    '/':operator.truediv}
                na = random.randint(1, 20)
                nb = random.randint(1, 20)
                op = random.choice(list(ops.keys()))
                txt = ("what is", na, op, nb,"?")
                ans = ops.get(op)(na,nb)

                root = Tk()
                root.geometry("300x320")
                root.title("Q&A")
                 
                def Take_input():
                    INPUT = inputtxt.get("1.0", "end-1c")
                    print(INPUT)
                    if(int(INPUT) == ans):
                        Output.insert(END, 'Correct')
                    else:
                        Output.insert(END, "Wrong answer")
                     
                l = Label(text = txt)
                inputtxt = Text(root, height = 10,
                                width = 25,
                                bg = "light yellow")
                 
                Output = Text(root, height = 5,
                              width = 25,
                              bg = "light cyan")
                 
                Display = Button(root, height = 2,
                                 width = 20,
                                 text ="Show",
                                 command = lambda:Take_input())
                 
                l.pack()
                inputtxt.pack()
                Display.pack()
                Output.pack()
                 
                mainloop()
        else:
            print("######################")
            print("#error invalid target#")
            print("######################")

